CREATE OR REPLACE PACKAGE orm_user_newss IS


    TYPE news_data IS RECORD(
        news_name user.user_name%TYPE,
        users_count INTEGER
    );


    TYPE tblnewsdata IS TABLE OF news_data;

    FUNCTION GetnewsData (news_name user.user_name%TYPE default null)
        RETURN tblnewsdata
        PIPELINED;

END orm_user_newss;




CREATE OR REPLACE PACKAGE BODY orm_user_newss IS

    FUNCTION GetnewsData (news_name user.user_name%TYPE default null)
    RETURN tblnewsdata
    PIPELINED
    IS

        TYPE news_cursor_type IS REF CURSOR;
        news_cursor  news_cursor_type;

        cursor_data news_data;
        query_str varchar2(1000);

    begin

        query_str :='select user_news.news_name, count(user_news.user_id)
                        from user_news ';

        -- optional part where
            if news_name is not null then
             query_str:= query_str||' where trim(user_news.news_name) = trim('''||news_name||''') ';
            end if;
        -- end optional part

        query_str := query_str||' group by user_news.news_name';



        OPEN news_cursor FOR query_str;
        LOOP
            FETCH news_cursor into cursor_data;
            exit when (news_cursor %NOTFOUND);

            PIPE ROW (cursor_data);

        END LOOP;


    END GetnewsData;

END user_news;