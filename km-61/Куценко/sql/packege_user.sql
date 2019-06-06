create or replace PACKAGE user IS


  TYPE users_name IS RECORD (
    user_id ORM_USER.user_id%TYPE,
    users_count INTEGER
    );

  TYPE place_name IS RECORD (
    place_id ORM_USER.network_id%TYPE,
    networks_count INTEGER
    );


  TYPE tu_nameIS TABLE OF users_name;

  FUNCTION user_id(user_id ORM_USER.user_id%TYPE default null)
    RETURN tu_usname
    PIPELINED;

  TYPE tp_name IS TABLE OF place_name;

  FUNCTION place_id(place_id ORM_USER.place_id%TYPE default null)
    return tp_name
    PIPELINED;
END user;



create or replace PACKAGE BODY orm_user_net IS

  FUNCTION user_id(user_id ORM_USER.user_id%TYPE default null)
    RETURN tu_name
    PIPELINED
  IS

    TYPE users_name_cursor_type IS REF CURSOR;
    user_id_cursor users_name_cursor_type;

    cursor_data users_name;
    query_str varchar2(1000);

  begin

    query_str := 'select ORM_USER.user_id, count(ORM_USER.user_id)
                        from ORM_USER';

    -- optional part where
    if user_id is not null then
      query_str := query_str || ' where trim(ORM_USER.user_id) = trim(''' || user_id || ''') ';
    end if;
    -- end optional part

    query_str := query_str || ' group by ORM_USER.user_id';


    OPEN user_id_cursor FOR query_str;
    LOOP
      FETCH user_id_cursor into cursor_data;
      exit when (user_id_cursor %NOTFOUND);

      PIPE ROW (cursor_data);

    END LOOP;

  END user_id;



END user;