CREATE OR REPLACE PACKAGE orm_user_group IS

    TYPE group_name IS RECORD(
        group_name ORM_GROUP.GROUP_NAME%TYPE,
        users_count INTEGER
    );

    TYPE tbldata IS TABLE OF skill_data;

    FUNCTION GetUsername (group_name RM_GROUP.GROUP_NAME%TYPE default null)
        RETURN tbldata
        PIPELINED;

END orm_user_group;

CREATE OR REPLACE PACKAGE BODY orm_user_group IS

    FUNCTION GetUsername (group_name ORM_GROUP.GROUP_NAME%TYPE default null)
    RETURN tbldata
    PIPELINED
    IS
        TYPE group_cursor_type IS REF CURSOR;
        group_cursor  group_cursor_type;
        cursor_data group_data;
        query_str varchar2(1000);

    begin
        query_str :='select ORM_USER.user_name
                        from ORM_USER_GROUP
                        where trim(ORM_USER_GROUP.group_name) = trim('''||group_name||''') ';

        query_str := query_str||'ORM_USER_GROUP.group_name';
        OPEN group_cursor FOR query_str;
        LOOP
            FETCH group_cursor into cursor_data;
            exit when (group_cursor %NOTFOUND);
            PIPE ROW (cursor_data);
        END LOOP;
    END GetUsername;
END orm_user_group;