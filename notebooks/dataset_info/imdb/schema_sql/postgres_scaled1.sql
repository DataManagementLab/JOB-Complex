DROP TABLE IF EXISTS "aka_name";
CREATE TABLE aka_name
(
    id            integer NOT NULL PRIMARY KEY,
    person_id     integer NOT NULL,
    name          character varying,
    imdb_index    character varying(3),
    name_pcode_cf character varying(11),
    name_pcode_nf character varying(11),
    surname_pcode character varying(11),
    md5sum        character varying(65)
);DROP TABLE IF EXISTS "aka_title";
CREATE TABLE aka_title
(
    id              integer NOT NULL PRIMARY KEY,
    movie_id        integer NOT NULL,
    title           character varying,
    imdb_index      character varying(4),
    kind_id         integer NOT NULL,
    production_year integer,
    phonetic_code   character varying(5),
    episode_of_id   integer,
    season_nr       integer,
    episode_nr      integer,
    note            character varying(72),
    md5sum          character varying(32)
);DROP TABLE IF EXISTS "cast_info";
CREATE TABLE cast_info
(
    id             integer NOT NULL PRIMARY KEY,
    person_id      integer NOT NULL,
    movie_id       integer NOT NULL,
    person_role_id integer,
    note           character varying,
    nr_order       integer,
    role_id        integer NOT NULL
);DROP TABLE IF EXISTS "char_name";
CREATE TABLE char_name
(
    id            integer           NOT NULL PRIMARY KEY,
    name          character varying NOT NULL,
    imdb_index    character varying(2),
    imdb_id       integer,
    name_pcode_nf character varying(5),
    surname_pcode character varying(5),
    md5sum        character varying(32)
);DROP TABLE IF EXISTS "comp_cast_type";
CREATE TABLE comp_cast_type
(
    id   integer               NOT NULL PRIMARY KEY,
    kind character varying(32) NOT NULL
);DROP TABLE IF EXISTS "company_name";
CREATE TABLE company_name
(
    id            integer           NOT NULL PRIMARY KEY,
    name          character varying NOT NULL,
    country_code  character varying(6),
    imdb_id       integer,
    name_pcode_nf character varying(5),
    name_pcode_sf character varying(5),
    md5sum        character varying(32)
);DROP TABLE IF EXISTS "company_type";
CREATE TABLE company_type
(
    id   integer NOT NULL PRIMARY KEY,
    kind character varying(32)
);DROP TABLE IF EXISTS "complete_cast";
CREATE TABLE complete_cast
(
    id         integer NOT NULL PRIMARY KEY,
    movie_id   integer,
    subject_id integer NOT NULL,
    status_id  integer NOT NULL
);DROP TABLE IF EXISTS "info_type";
CREATE TABLE info_type
(
    id   integer               NOT NULL PRIMARY KEY,
    info character varying(32) NOT NULL
);DROP TABLE IF EXISTS "keyword";
CREATE TABLE keyword
(
    id            integer           NOT NULL PRIMARY KEY,
    keyword       character varying NOT NULL,
    phonetic_code character varying(5)
);DROP TABLE IF EXISTS "kind_type";
CREATE TABLE kind_type
(
    id   integer NOT NULL PRIMARY KEY,
    kind character varying(15)
);DROP TABLE IF EXISTS "link_type";
CREATE TABLE link_type
(
    id   integer               NOT NULL PRIMARY KEY,
    link character varying(32) NOT NULL
);DROP TABLE IF EXISTS "movie_companies";
CREATE TABLE movie_companies
(
    id              integer NOT NULL PRIMARY KEY,
    movie_id        integer NOT NULL,
    company_id      integer NOT NULL,
    company_type_id integer NOT NULL,
    note            character varying
);DROP TABLE IF EXISTS "movie_info_idx";
CREATE TABLE movie_info_idx
(
    id           integer           NOT NULL PRIMARY KEY,
    movie_id     integer           NOT NULL,
    info_type_id integer           NOT NULL,
    info         character varying NOT NULL,
    note         character varying(1)
);DROP TABLE IF EXISTS "movie_keyword";
CREATE TABLE movie_keyword
(
    id         integer NOT NULL PRIMARY KEY,
    movie_id   integer NOT NULL,
    keyword_id integer NOT NULL
);DROP TABLE IF EXISTS "movie_link";
CREATE TABLE movie_link
(
    id              integer NOT NULL PRIMARY KEY,
    movie_id        integer NOT NULL,
    linked_movie_id integer NOT NULL,
    link_type_id    integer NOT NULL
);DROP TABLE IF EXISTS "name";
CREATE TABLE name
(
    id            integer           NOT NULL PRIMARY KEY,
    name          character varying NOT NULL,
    imdb_index    character varying(9),
    imdb_id       integer,
    gender        character varying(1),
    name_pcode_cf character varying(5),
    name_pcode_nf character varying(5),
    surname_pcode character varying(5),
    md5sum        character varying(32)
);DROP TABLE IF EXISTS "role_type";
CREATE TABLE role_type
(
    id   integer               NOT NULL PRIMARY KEY,
    role character varying(32) NOT NULL
);DROP TABLE IF EXISTS "title";
CREATE TABLE title
(
    id              integer           NOT NULL PRIMARY KEY,
    title           character varying NOT NULL,
    imdb_index      character varying(5),
    kind_id         integer           NOT NULL,
    production_year integer,
    imdb_id         integer,
    phonetic_code   character varying(5),
    episode_of_id   integer,
    season_nr       integer,
    episode_nr      integer,
    series_years    character varying(49),
    md5sum          character varying(32)
);DROP TABLE IF EXISTS "movie_info";
CREATE TABLE movie_info
(
    id           integer           NOT NULL PRIMARY KEY,
    movie_id     integer           NOT NULL,
    info_type_id integer           NOT NULL,
    info         character varying NOT NULL,
    note         character varying
);DROP TABLE IF EXISTS "person_info";
CREATE TABLE person_info
(
    id           integer           NOT NULL PRIMARY KEY,
    person_id    integer           NOT NULL,
    info_type_id integer           NOT NULL,
    info         character varying NOT NULL,
    note         character varying
);