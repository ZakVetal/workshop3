
create or replace PACKAGE editors_search IS

  TYPE editor_search_data IS RECORD
    (
    user_id orm_user.user_id%TYPE,
    user_name orm_user.user_name%TYPE,
    user_login orm_user.user_login%TYPE,
    file_id orm_file.file_id%TYPE,
    file_name orm_file.file_name%TYPE,
    file_date orm_file.file_date%TYPE,
    file_type orm_file.file_type%TYPE,
    file_context  orm_file.file_context%TYPE
    );

  TYPE editor_search_table IS TABLE OF editor_search_data;

  FUNCTION find(file_name orm_file.file_name%TYPE default null,
                user_name orm_user.user_name%TYPE default null)
    RETURN editor_search_table
    PIPELINED;

END editors_search;

create or replace PACKAGE BODY editors_search IS

  FUNCTION find(file_name orm_file.file_name%TYPE default null,
                 user_name orm_user.user_name%TYPE default null)
    RETURN editor_search_table
    PIPELINED
  IS

    TYPE cursor_type IS REF CURSOR;
    search_cursor cursor_type;

    editor_row editor_search_data;
    query_s varchar2(2000);
    where_query varchar2(300);

  BEGIN
    where_query := ' where 1=1 ';

    query_s := 'select user_id, user_name, user_login, file_id, file_name, file_date, file_type, file_context ' ||
    'from orm_user natural join orm_file natural join orm_file_editor';

    if file_name is not NULL then
        where_query := where_query || ' and file_name = ''' || file_name || ''' ';
    end if;

    if user_name is not NULL then
            where_query := where_query || 'and user_name = ''' || user_name || ''' ';
    end if;

    query_s := query_s || where_query;

    OPEN search_cursor FOR query_s;
    LOOP
      FETCH search_cursor into editor_row;
      exit when (search_cursor %NOTFOUND);

      PIPE ROW (editor_row);
    end loop;
    CLOSE search_cursor;

  END find;

END editors_search;
