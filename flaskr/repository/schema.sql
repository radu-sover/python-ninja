drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    title text not null,
    text text not null
);

drop table if exists statistics;
create table statistics (
  name text primary key,
  count integer not null
);
