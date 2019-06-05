create or replace package orm_user_package IS

    TYPE user_data IS RECORD(
        first_name "SYSTEM"."ORM_USER".user_first_name%TYPE,
        last_name "SYSTEM"."ORM_USER".user_last_name%TYPE,
        event_count INTEGER
    );

    TYPE tbluserdata IS TABLE OF user_data;

    FUNCTION GetUserData (first_name "SYSTEM"."ORM_USER".user_first_name%TYPE default null, last_name "SYSTEM"."ORM_USER".user_last_name%TYPE default null)
        RETURN tbluserdata
        PIPELINED;

END orm_user_package;
/

CREATE OR REPLACE PACKAGE BODY orm_user_package IS

    FUNCTION GetUserData (first_name "SYSTEM"."ORM_USER".user_first_name%TYPE default null, last_name "SYSTEM"."ORM_USER".user_last_name%TYPE default null)
        RETURN tbluserdata
        PIPELINED
        IS
            TYPE user_cursor_type IS REF CURSOR;
            user_cursor user_cursor_type;

            cursor_data user_data;
            query_str varchar2(1000);

        begin
            query_str := 'select "SYSTEM"."ORM_ATTENDANCE".user_id, "SYSTEM"."ORM_USER".user_first_name, "SYSTEM"."ORM_USER".user_last_name, count("SYSTEM"."ORM_ATTENDANCE".event_id) as event_count';
            query_str := query_str||'from "SYSTEM"."ORM_ATTENDANCE" LEFT JOIN "SYSTEM"."ORM_USER" ON "SYSTEM"."ORM_ATTENDANCE".user_id="SYSTEM"."ORM_USER".user_id';

            if (first_name is not null) and (last_name is not null) then
                query_str := query_str||'where trim("SYSTEM"."ORM_USER".user_first_name)=trim('''||first_name||''') and trim("SYSTEM"."ORM_USER".user_last_name)=trim('''||last_name||''')';
            end if;
            query_str := query_str||'GROUP BY ("SYSTEM"."ORM_ATTENDANCE".user_id, "SYSTEM"."ORM_USER".user_first_name);';

            OPEN user_cursor FOR query_str;
            LOOP
                FETCH user_cursor into cursor_data;
                exit when (user_cursor %NOTFOUND);

                PIPE ROW (cursor_data);
            END LOOP;
        END GetUserData;
    END orm_user_package;