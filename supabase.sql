-- Supabase AI is experimental and may produce incorrect answers
-- Always verify the output before executing

drop table if exists jobs;

create table
  jobs (
    id bigint primary key generated always as identity,
    title text,
    description text,
    company text,
    location text,
    requirements text,
    posted_date timestamp with time zone default now()
  );
drop table if exists candidates;

create table
  candidates (
    id bigint primary key generated always as identity,
    first_name text,
    last_name text,
    email text unique,
    skills text,
    resume_url text
  );


b22N%eFYE8bumQw
QpcnGWmMbrOKCe0M