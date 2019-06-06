CREATE TABLE "User"(full_name varchar2(100), "location" varchar2(100) NOT NULL);
CREATE TABLE TODOList(full_name varchar2(100), "date" DATE, "name" VARCHAR2(50));
CREATE TABLE Action(full_name varchar2(100), "date" DATE, "name" VARCHAR2(50),
time_open DATE, time_close DATE, description VARCHAR2(255) NOT NULL,
execution_time NUMBER(8), "location" VARCHAR2(255));

ALTER TABLE "User"
ADD CONSTRAINT full_name_pk PRIMARY KEY (full_name);

ALTER TABLE TODOList
ADD CONSTRAINT name_date_user_pk PRIMARY KEY (full_name, "date", "name");
ALTER TABLE TODOList
ADD CONSTRAINT user_has_lists_fk FOREIGN KEY (full_name) REFERENCES "User"(full_name);

ALTER TABLE Action
ADD CONSTRAINT time_list_pk PRIMARY KEY (full_name, "date", "name", time_open, time_close);
ALTER TABLE Action
ADD CONSTRAINT TODOList_contains_actions FOREIGN KEY(full_name, "date", "name") REFERENCES TODOList(full_name, "date", "name");

INSERT ALL
INTO "User" VALUES('Vasiliy Zaytsev', 'KPI')
INTO "User" VALUES('Tony Stark', 'Cinema')
INTO "User" VALUES('Lexa Subotin', 'The Wall')
INTO "User" VALUES('Aria Stark', 'HDRezka')
SELECT * FROM DUAL;

INSERT ALL
INTO TODOList VALUES('Tony Stark', TO_DATE('26-04-2019 16:30:00'), 'Save the world')
INTO TODOList VALUES('Tony Stark', TO_DATE('26-04-2019 18:30:00'), 'Click with fingers')
INTO TODOList VALUES('Aria Stark', TO_DATE('28-04-2019 19:00:00'), 'Save the world')
INTO TODOList VALUES('Lexa Subotin', TO_DATE('05-06-2019 19:00:00'), 'Get Lost')
SELECT * FROM DUAL;

INSERT ALL
INTO Action VALUES('Tony Stark', TO_DATE('26-04-2019 16:30:00'), 'Save the world',
TO_DATE('26-04-2019 18:30:00'), TO_DATE('26-04-2019 19:00:00'),
'get the gauntlet', 30*60, 'cinema')
INTO Action VALUES('Tony Stark', TO_DATE('26-04-2019 18:30:00'), 'Click with fingers',
TO_DATE('26-04-2019 19:10:00'), TO_DATE('26-04-2019 19:11:00'),
'click your fingers', 60, 'cinema')
INTO Action VALUES('Aria Stark', TO_DATE('28-04-2019 19:00:00'), 'Save the world',
TO_DATE('28-04-2019 18:59:00'), TO_DATE('28-04-2019 19:00:00'),
'jump on the night king', 60, 'cinema')
INTO Action VALUES('Aria Stark', TO_DATE('28-04-2019 19:00:00'), 'Save the world',
TO_DATE('28-04-2019 19:00:00'), TO_DATE('28-04-2019 19:01:00'),
'make the bloody surprise to everyone', 60, 'cinema')
SELECT * FROM DUAL;