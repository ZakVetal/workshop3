create table students
(
  student_number varchar2(32) not null,
  ssn            integer      not null,
  firstname      varchar2(30) not null,
  middlename     varchar2(30),
  lastname       varchar2(30) not null,
  birthdate      date
);

alter table students
  add constraint student_number_pk primary key (student_number);

CREATE TRIGGER student_number_generation
  BEFORE INSERT
  ON students
  FOR EACH ROW
BEGIN
  :new.student_number := SYS_GUID();
END;

create table groups
(
  group_identifier varchar2(32) not null,
  title            varchar2(10) not null,
  creation_date    date,
  expiration_date  date
);

alter table groups
  add constraint group_identifier_pk primary key (group_identifier);
alter table groups
  add constraint unique_groups unique (title, creation_date, expiration_date);

CREATE TRIGGER group_identifier_generation
  BEFORE INSERT
  ON groups
  FOR EACH ROW
BEGIN
  :new.group_identifier := SYS_GUID();
END;

create table studentgroup
(
  id               varchar2(32) not null,
  student_number   varchar2(32) not null,
  group_identifier varchar2(32) not null,
  start_date       date         not null,
  end_date         date         null
);

CREATE TRIGGER studentgroup_id_generation
  BEFORE INSERT
  ON studentgroup
  FOR EACH ROW
BEGIN
  :new.id := SYS_GUID();
END;

alter table studentgroup
  add constraint studentgroup_pk primary key (student_number, group_identifier, start_date, end_date);
alter table studentgroup
  add constraint student_number_fk foreign key (student_number) references students (student_number);
alter table studentgroup
  add constraint group_identifier_fk foreign key (group_identifier) references groups (group_identifier);


create or replace PACKAGE student_search IS

  TYPE student_data IS RECORD
    (
    student_number STUDENTS.STUDENT_NUMBER%TYPE,
    firstname STUDENTS.FIRSTNAME%TYPE,
    middlename STUDENTS.MIDDLENAME%TYPE,
    lastname STUDENTS.LASTNAME%TYPE,
    ssn STUDENTS.SSN%TYPE,
    birthdate STUDENTS.Birthdate%TYPE
    );

  TYPE student_data_table IS TABLE OF student_data;

  FUNCTION find(firstname STUDENTS.FIRSTNAME%TYPE default null,
                lastname STUDENTS.LASTNAME%TYPE default null,
                group_title GROUPS.TITLE%TYPE default null)
    RETURN student_data_table
    PIPELINED;

END student_search;


create or replace PACKAGE BODY student_search IS

  FUNCTION find(firstname STUDENTS.FIRSTNAME%TYPE default null,
                lastname STUDENTS.LASTNAME%TYPE default null,
                group_title GROUPS.TITLE%TYPE default null)
    RETURN student_data_table
    PIPELINED
  IS
    TYPE student_cursor_type IS REF CURSOR;
    student_cursor student_cursor_type;

    TYPE string_list is varray(3) of varchar2(100);
    filters string_list := string_list();
    filters_quantity integer := 0;

    student student_data;
    query varchar2(2000);
    filter_query varchar2(300);

  BEGIN
    filter_query := ' where ';

    query := 'SELECT students.student_number, ' ||
            '       students.firstname, ' ||
            '       students.middlename, ' ||
            '       students. lastname, ' ||
            '       students.ssn, ' ||
            '       students.birthdate FROM students';

    if firstname is not null then
        filters_quantity := filters_quantity + 1;
        filters.extend;
        filters(filters_quantity) := ' students.firstname = ''' || firstname || ''' ';
    end if;

    if lastname is not null then
        filters_quantity := filters_quantity + 1;
        filters.extend;
        filters(filters_quantity) := ' students.lastname = ''' || lastname || ''' ';
    end if;

    if group_title is not null then
        filters_quantity := filters_quantity + 1;
        filters.extend;
        filters(filters_quantity) := ' groups.title = ''' || group_title || ''' ';
        query := query || ' join studentgroup on students.student_number = studentgroup.student_number' ||
                               '         join groups on groups.group_identifier = studentgroup.group_identifier ';
    end if;

    if filters_quantity != 0 then
         for i in 1..filters_quantity loop
            if i != filters_quantity then
                filter_query := filter_query ||  filters(i)  || ' and ';
            else 
                 filter_query := filter_query ||  filters(i);
            end if;
        end loop;
       query := query || filter_query;
    end if;


    OPEN student_cursor FOR query;
    LOOP
      FETCH student_cursor into student;
      exit when (student_cursor %NOTFOUND);

      PIPE ROW (student);
    end loop;
    CLOSE student_cursor;

  END find;

END student_search;