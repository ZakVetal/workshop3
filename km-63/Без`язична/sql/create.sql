create table user(email varchar(20),password varchar(13));
alter table user add constraint pk_email primary  key(email);

create table calendar (date varchar(20));
alter table calendar add constraint pk_date primary  key(date);
alter table calendar add constraint
fk_email key referenses user(email);

create table event( name varchar(20),email varchar(20),date date, time varchar(20), longitude varchar(20),latitude varchar(20));
alter table event add constraint pk_name primary  key(name);
alter table event add constraint
fk2_email key referenses user(email);
alter table event add constraint
fk_date key referenses calendar(date);