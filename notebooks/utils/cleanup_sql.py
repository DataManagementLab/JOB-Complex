from functools import lru_cache

import sqlparse

from utils.parse_query import get_preds_from_query, extract_filter_jon_conditions


@lru_cache(maxsize=None)
def cleanup_sql(sql: str) -> str:
    sql = sql.strip()
    if not sql.endswith(';'):
        sql = sql + ';'

    parsed_query = sqlparse.parse(sql)

    predicates, num_disjunctions = get_preds_from_query(parsed_query, flatten_disjunction=True)
    filter_conds, filter_operators, filter_cols, join_conds = extract_filter_jon_conditions(predicates)

    # search for duplicate join conditions
    duplicate_conditions = []
    for i in range(len(join_conds)):
        join_cond1 = join_conds[i]
        for k in range(i + 1, len(join_conds)):
            join_cond2 = join_conds[k]
            if (str(join_cond1.left) == str(join_cond2.left) and str(join_cond1.right) == str(join_cond2.right)) or (
                    str(join_cond1.left) == str(join_cond2.right) and str(join_cond1.right) == str(join_cond2.left)):
                if str(join_cond2) not in duplicate_conditions:
                    # add join condition to duplicate conditions
                    duplicate_conditions.append(str(join_cond2))

    # remove join conditions that are useless: t1.c1=t1.c1
    superfluous_conditions = []
    for cond in join_conds:
        if str(cond.left) == str(cond.right) and str(cond) not in superfluous_conditions:
            superfluous_conditions.append(str(cond))

    cleaned_sql = sql

    # remove superfluous conditions
    for cond in superfluous_conditions:
        if cond in duplicate_conditions:
            # remove from duplicate conditions - we process it only once
            duplicate_conditions.remove(cond)

        assert str(cond) in cleaned_sql, f'Condition \'{str(cond)}\' not found in SQL: {cleaned_sql} / {sql}'
        cleaned_sql = cleaned_sql.replace(f' {cond}', '')

    # remove duplicate conditions
    for cond in duplicate_conditions:
        assert str(cond) in cleaned_sql, f'Condition \'{str(cond)}\' not found in SQL: {cleaned_sql} / {sql}'

        # count if condition appears only once
        if cleaned_sql.count(str(cond)) == 1:
            # this is a swapped duplicate connection
            cleaned_sql = cleaned_sql.replace(f' {cond}', '')
        else:
            # keep only first occurrence of the condition
            cleaned_sql = cleaned_sql.replace(f' {cond}', '', cleaned_sql.count(str(cond)) - 1)

    # remove duplicate whitespace
    cleaned_sql = ' '.join(cleaned_sql.split())

    # remove repeated AND
    while 'AND AND' in cleaned_sql:
        # replace AND AND with AND
        # this is a workaround for the sqlparse library
        # which does not remove duplicate ANDs
        # and creates a lot of noise in the SQL
        cleaned_sql = cleaned_sql.replace('AND AND', 'AND')

    # if query ends with AND -> remove trailing and
    assert cleaned_sql.endswith(';'), f'Query does not end with ;: {cleaned_sql}'
    if cleaned_sql[:-1].strip().endswith('AND'):
        # remove the and
        cleaned_sql = cleaned_sql[:-1].strip()[:-3].strip() + ';'

    # remove ::text casts
    cleaned_sql = cleaned_sql.replace('::text ', ' ')
    cleaned_sql = cleaned_sql.replace('::text;', ';')

    return cleaned_sql
