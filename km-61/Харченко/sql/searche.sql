create or replace PACKAGE editors_search IS

  TYPE editor_search_data IS RECORD
    (
    new_id orm_News.new_id%TYPE,
    news_name orm_News.news_name%TYPE,
    text orm_News.text%TYPE,
    sourse orm_News.sourse%TYPE,
    neme_class orm_orm_class.neme_class%TYPE,
    nick orm_Date.file_date%TYPE,
    new_id_read orm_Date.new_id%TYPE,
    date_read orm_Date.date_read%TYPE
    );

  TYPE search_table IS TABLE OF earch_data;

  FUNCTION find(nick orm_Date.file_date%TYPE default null,
                news_name orm_News.news_name%TYPE default null,
				date_read orm_Date.date_read%TYPE default null)
    RETURN search_table
    PIPELINED;

END editors_search;

create or replace PACKAGE BODY editors_search IS

 FUNCTION find(nick orm_Date.file_date%TYPE default null,
                news_name orm_News.news_name%TYPE default null,
				date_read orm_Date.date_read%TYPE default null)
    RETURN search_table
    PIPELINED
  IS

    TYPE cursor_type IS REF CURSOR;
    search_cursor cursor_type;

    editor_row editor_search_data;
    query_s varchar2(15);
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