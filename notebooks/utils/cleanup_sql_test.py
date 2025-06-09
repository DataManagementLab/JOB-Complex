import unittest

from cleanup_sql import cleanup_sql


class CleanupSQLTest(unittest.TestCase):
    def test_cleanup_sql(self):
        sql1 = '''SELECT MIN(mi.info)     AS movie_budget,
                         MIN(mi_idx.info) AS movie_votes,
                         MIN(n.name)      AS writer,
                         MIN(t.title)     AS complete_gore_movie
                  FROM complete_cast AS cc,
                       comp_cast_type AS cct1,
                       comp_cast_type AS cct2,
                       cast_info AS ci,
                       info_type AS it1,
                       info_type AS it2,
                       keyword AS k,
                       movie_info AS mi,
                       movie_info_idx AS mi_idx,
                       movie_keyword AS mk,
                       name AS n,
                       title AS t,
                       char_name AS c
                  WHERE cct1.kind IN ('cast', 'crew')
                    AND cct2.kind = 'complete+verified'
                    AND ci.note IN ('(writer)', '(head writer)', '(written by)', '(story)', '(story editor)')
                    AND it1.info = 'genres'
                    AND it2.info = 'votes'
                    AND k.keyword IN ('murder', 'violence', 'blood', 'gore', 'death', 'female-nudity', 'hospital')
                    AND mi.info IN ('Horror', 'Thriller')
                    AND n.gender = 'm'
                    AND t.production_year > 2000
                    AND (t.title LIKE '%Freddy%' OR t.title LIKE '%Jason%' OR t.title LIKE 'Saw%')
                    AND t.id = mi.movie_id
                    AND t.id = mi_idx.movie_id
                    AND t.id = ci.movie_id
                    AND t.id = mk.movie_id
                    AND t.id = cc.movie_id
                    AND ci.movie_id = mi.movie_id
                    AND ci.movie_id = mi_idx.movie_id
                    AND ci.movie_id = mk.movie_id
                    AND ci.movie_id = cc.movie_id
                    AND mi.movie_id::text = mi_idx.movie_id
                    AND mi.movie_id = mk.movie_id
                    AND mi.movie_id = cc.movie_id
                    AND mi_idx.movie_id = mk.movie_id
                    AND mi_idx.movie_id = cc.movie_id
                    AND mk.movie_id = cc.movie_id
                    AND n.id = ci.person_id
                    AND it1.id = mi.info_type_id
                    AND it2.id = mi_idx.info_type_id
                    AND k.id = mk.keyword_id
                    AND cct1.id = cc.subject_id
                    AND cct2.id = cc.status_id
                    AND c.name_pcode_nf = n.name_pcode_nf
                    AND c.surname_pcode = n.surname_pcode
                    AND c.surname_pcode = c.surname_pcode
                    AND n.name_pcode_nf = c.name_pcode_nf
                    AND n.surname_pcode = c.surname_pcode;'''
        sql_cleaned = cleanup_sql(sql1)

        expected = '''SELECT MIN(mi.info)     AS movie_budget,
                             MIN(mi_idx.info) AS movie_votes,
                             MIN(n.name)      AS writer,
                             MIN(t.title)     AS complete_gore_movie
                      FROM complete_cast AS cc,
                           comp_cast_type AS cct1,
                           comp_cast_type AS cct2,
                           cast_info AS ci,
                           info_type AS it1,
                           info_type AS it2,
                           keyword AS k,
                           movie_info AS mi,
                           movie_info_idx AS mi_idx,
                           movie_keyword AS mk,
                           name AS n,
                           title AS t,
                           char_name AS c
                      WHERE cct1.kind IN ('cast', 'crew')
                        AND cct2.kind = 'complete+verified'
                        AND ci.note IN ('(writer)', '(head writer)', '(written by)', '(story)', '(story editor)')
                        AND it1.info = 'genres'
                        AND it2.info = 'votes'
                        AND k.keyword IN ('murder', 'violence', 'blood', 'gore', 'death', 'female-nudity', 'hospital')
                        AND mi.info IN ('Horror', 'Thriller')
                        AND n.gender = 'm'
                        AND t.production_year > 2000
                        AND (t.title LIKE '%Freddy%' OR t.title LIKE '%Jason%' OR t.title LIKE 'Saw%')
                        AND t.id = mi.movie_id
                        AND t.id = mi_idx.movie_id
                        AND t.id = ci.movie_id
                        AND t.id = mk.movie_id
                        AND t.id = cc.movie_id
                        AND ci.movie_id = mi.movie_id
                        AND ci.movie_id = mi_idx.movie_id
                        AND ci.movie_id = mk.movie_id
                        AND ci.movie_id = cc.movie_id
                        AND mi.movie_id = mi_idx.movie_id
                        AND mi.movie_id = mk.movie_id
                        AND mi.movie_id = cc.movie_id
                        AND mi_idx.movie_id = mk.movie_id
                        AND mi_idx.movie_id = cc.movie_id
                        AND mk.movie_id = cc.movie_id
                        AND n.id = ci.person_id
                        AND it1.id = mi.info_type_id
                        AND it2.id = mi_idx.info_type_id
                        AND k.id = mk.keyword_id
                        AND cct1.id = cc.subject_id
                        AND cct2.id = cc.status_id
                        AND c.name_pcode_nf = n.name_pcode_nf
                        AND c.surname_pcode = n.surname_pcode;'''
        # remove indentation and newlines for comparison
        expected = expected.replace('\n', ' ').replace('  ', ' ')
        # remove duplicate spaces
        expected = ' '.join(expected.split())
        self.assertEqual(expected, sql_cleaned)

        sql2 = '''SELECT MIN(cn1.name)     AS first_company,
                         MIN(cn2.name)     AS second_company,
                         MIN(mi_idx1.info) AS first_rating,
                         MIN(mi_idx2.info) AS second_rating,
                         MIN(t1.title)     AS first_movie,
                         MIN(t2.title)     AS second_movie
                  FROM company_name AS cn1,
                       company_name AS cn2,
                       info_type AS it1,
                       info_type AS it2,
                       kind_type AS kt1,
                       kind_type AS kt2,
                       link_type AS lt,
                       movie_companies AS mc1,
                       movie_companies AS mc2,
                       movie_info_idx AS mi_idx1,
                       movie_info_idx AS mi_idx2,
                       movie_link AS ml,
                       title AS t1,
                       title AS t2
                  WHERE cn1.country_code != '[us]' AND it1.info = 'rating' AND it2.info = 'rating' AND kt1.kind IN ('tv series', 'episode') AND kt2.kind IN ('tv series', 'episode') AND lt.link IN ('sequel', 'follows', 'followed by') AND mi_idx2.info < '3.5' AND t2.production_year BETWEEN 2000 AND 2010 AND lt.id = ml.link_type_id AND t1.id = ml.movie_id AND t2.id = ml.linked_movie_id AND it1.id = mi_idx1.info_type_id AND t1.id = mi_idx1.movie_id AND kt1.id = t1.kind_id AND cn1.id = mc1.company_id AND t1.id = mc1.movie_id AND ml.movie_id = mi_idx1.movie_id AND ml.movie_id = mc1.movie_id AND mi_idx1.movie_id = mc1.movie_id AND it2.id = mi_idx2.info_type_id AND t2.id = mi_idx2.movie_id AND kt2.id = t2.kind_id AND cn2.id = mc2.company_id AND t2.id = mc2.movie_id AND ml.linked_movie_id = mi_idx2.movie_id AND ml.linked_movie_id = mc2.movie_id AND mi_idx2.movie_id = mc2.movie_id AND cn1.name_pcode_nf = cn2.name_pcode_nf AND cn1.name_pcode_nf = cn2.name_pcode_nf AND cn2.name_pcode_nf = cn1.name_pcode_nf AND cn2.name_pcode_nf = cn2.name_pcode_nf;'''
        sql_cleaned2 = cleanup_sql(sql2)


if __name__ == '__main__':
    unittest.main()
