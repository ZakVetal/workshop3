CREATE OR REPLACE PACKAGE orm_places IS


    TYPE skill_data IS RECORD(
        user_locale ORM_USER.USER_LOCALE%TYPE,
        places_date DATE
    );


    TYPE tblskilldata IS TABLE OF user_data;

    FUNCTION GetUSERData (user_locale ORM_USER.USER_LOCALE%TYPE default null)
        RETURN tblskilldata
        PIPELINED;

END orm_places;




CREATE OR REPLACE PACKAGE BODY orm_places IS

    FUNCTION GetUSERData (user_locale ORM_USER.USER_LOCALE%TYPE default null)
    RETURN tblskilldata
    PIPELINED
    IS

        TYPE user_cursor_type IS REF CURSOR;
        user_cursor  user_cursor_type;

        cursor_data user_data;
        query_str varchar2(1000);

    begin

        query_str :='select ORM_PLACES.user_locale, count(ORM_PLACES.places_date)
                        from ORM_PLACES ';

        -- optional part where
            if user_locale is not null then
             query_str:= query_str||' where trim(ORM_PLACES.user_locale) = trim('''|| user_locale ||''') ';
            end if;
        -- end optional part

        query_str := query_str||' group by ORM_PLACES.user_locale';



        OPEN user_cursor FOR query_str;
        LOOP
            FETCH user_cursor into cursor_data;
            exit when (user_cursor %NOTFOUND);

            PIPE ROW (cursor_data);

        END LOOP;


    END GetSUserData;

ENDorm_places
