CREATE OR REPLACE PACKAGE orm_board IS


    TYPE message_data IS RECORD(
         time_send ORM_MESSAGE.TIME_SEND%TYPE,
         message_count INTEGER
    );


    TYPE tbls IS TABLE OF message_data;

    FUNCTION GetMessageData ( time_send ORM_MESSAGE.TIME_SEND%TYPE default null)
        RETURN tblmessagedata
        PIPELINED;

END orm_board;




CREATE OR REPLACE PACKAGE BODY orm_board IS

    FUNCTION GetMessageData (time_send ORM_MESSAGE.TIME_SEND%TYPE default null)
    RETURN tblmessagedata
    PIPELINED
    IS

        TYPE message_cursor_type IS REF CURSOR;
        message_cursor  message_cursor_type;

        cursor_data message_data ;
        query_str varchar2(1000);

    query_str :='select ORM_BOARD.time_send, count(ORM_BOARD.user_phone)
                        from ORM_BOARD ';

        -- optional part where
            if time_send is not null then
             query_str:= query_str||' where trim(ORM_BOARD.time_send) = trim('''||skill_name||''') ';
            end if;
        -- end optional part

        query_str := query_str||' group by ORM_BOARD.time_send';



        OPEN message_cursor FOR query_str;
        LOOP
            FETCH message_cursorr into cursor_data;
            exit when (message_cursor %NOTFOUND);

            PIPE ROW (cursor_data);

        END LOOP;


    END GetGetMessageDataData;

END orm_board;
