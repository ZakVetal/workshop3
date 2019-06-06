create or replace PACKAGE orm_user_net IS


  TYPE users_name IS RECORD (
    user_id ORM_USER_USE_NETWORK.user_id%TYPE,
    users_count INTEGER
    );

  TYPE networks_name IS RECORD (
    network_id ORM_USER_USE_NETWORK.network_id%TYPE,
    networks_count INTEGER
    );


  TYPE table_usname IS TABLE OF users_name;

  FUNCTION user_id(user_id ORM_USER_USE_NETWORK.user_id%TYPE default null)
    RETURN table_usname
    PIPELINED;

  TYPE table_netname IS TABLE OF networks_name;

  FUNCTION network_id(network_id ORM_USER_USE_NETWORK.network_id%TYPE default null)
    return table_netname
    PIPELINED;
END orm_user_net;



create or replace PACKAGE BODY orm_user_net IS

  FUNCTION user_id(user_id ORM_USER_USE_NETWORK.user_id%TYPE default null)
    RETURN table_usname
    PIPELINED
  IS

    TYPE users_name_cursor_type IS REF CURSOR;
    user_id_cursor users_name_cursor_type;

    cursor_data users_name;
    query_str varchar2(1000);

  begin

    query_str := 'select ORM_USER_USE_NETWORK.user_id, count(ORM_USER_USE_NETWORK.user_id)
                        from ORM_USER_USE_NETWORK ';

    -- optional part where
    if user_id is not null then
      query_str := query_str || ' where trim(ORM_USER_USE_NETWORK.user_id) = trim(''' || user_id || ''') ';
    end if;
    -- end optional part

    query_str := query_str || ' group by ORM_USER_USE_NETWORK.user_id';


    OPEN user_id_cursor FOR query_str;
    LOOP
      FETCH user_id_cursor into cursor_data;
      exit when (user_id_cursor %NOTFOUND);

      PIPE ROW (cursor_data);

    END LOOP;

  END user_id;


  FUNCTION network_id(network_id ORM_USER_USE_NETWORK.network_id%TYPE default null)
    RETURN table_netname
    PIPELINED
  IS

    TYPE networks_name_cursor_type IS REF CURSOR;
    network_id_cursor networks_name_cursor_type;

    cursor_info networks_name;
    query_str varchar2(1000);

  begin

    query_str := 'select ORM_USER_USE_NETWORK.network_id, count(ORM_USER_USE_NETWORK.network_id)
                        from ORM_USER_USE_NETWORK ';

    -- optional part where
    if network_id is not null then
      query_str := query_str || ' where trim(ORM_USER_USE_NETWORK.network_id) = trim(''' || network_id || ''') ';
    end if;
    -- end optional part

    query_str := query_str || ' group by ORM_USER_USE_NETWORK.network_id';


    OPEN network_id_cursor FOR query_str;
    LOOP
      FETCH network_id_cursor into cursor_info;
      exit when (network_id_cursor %NOTFOUND);

      PIPE ROW (cursor_info);

    END LOOP;

  END network_id;

END orm_user_net;