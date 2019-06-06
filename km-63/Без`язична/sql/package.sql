create or replace package my_pack is
  procedure create_user(

                            ann in user.email%TYPE,
                            b12432 in user.password%TYPE
                            status out varchar2
                        );
     procedure update_user(

                            kate in user.email%TYPE,
                            b1244432 in user.password%TYPE
                            status out varchar2
                        );
     procedure drop_user(

                            ann in user.email%TYPE,
                            status out varchar2
                        );
      procedure new_Calendar(

                            12/03/2019 in calendar.date%TYPE,
                            ann in calendar.email%TYPE,
                            status out varchar2
                        );
     procedure update_Calendar(

                            12/05/2019 in calendar.date%TYPE,
                            kate in calendar.email%TYPE,
                            status out varchar2


                        );
     procedure drop_Calendar(

                            12/03/2019 in calendar.date%TYPE
                            status out varchar2
                        );
      procedure create_Event(

                            ann in event.email%TYPE,
                            birthday in event.name%TYPE,
                            23/12/2019 in event.date%TYPE,
                            18:00 in event.time%TYPE,
                            27.17 in event.longtitude%TYPE,
                            54.12 in event.latitude%TYPE
                            status out varchar2


                        );

     procedure drop_Event(
                            23/12/2019 in event.date%TYPE
                            status out varchar2
                        );

    FUNCTION Getuser (event.email INTEGER default null,event.name INTEGER default null, x ,y )
        RETURN tblsour
        PIPELINED;
            end my_pack;

create or replace package body my_pack is
FUNCTION GetUser (a event.emailk%TYPE ,b event.name%TYPE )
        begin

        our_query:='select event.email from Event where our_query = trim('''||ann||''') and event.name= trim('''||birthday||''')';

        query_str := query_str||' group by ORM_event.name';



        OPEN mod FOR query_str;
        LOOP
            FETCH mod into cursor_data;
            exit when (mod %NOTFOUND);

            PIPE ROW (mod);

        END LOOP;

            end my_pack;

