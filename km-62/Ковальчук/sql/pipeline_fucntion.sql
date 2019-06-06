CREATE OR REPLACE PACKAGE orm_user_Document IS


    TYPE Document_data IS RECORD(
        patch_file ORM_Document.patch_file%TYPE,
        users_count INTEGER
    );


    TYPE tblDocumentdata IS TABLE OF Document_data;

    FUNCTION GetDocumentData (patch_file ORM_Document.patch_file%TYPE default null)
        RETURN tblDocumentdata
        PIPELINED;

END orm_user_Document;




CREATE OR REPLACE PACKAGE BODY orm_user_Document IS

    FUNCTION GetDocumentData (patch_file ORM_Document.patch_file%TYPE default null)
    RETURN tblDocumentdata
    PIPELINED
    IS

        TYPE Document_cursor_type IS REF CURSOR;
        Document_cursor  Document_cursor_type;

        cursor_data Document_data;
        query_str varchar2(1000);

    begin

        query_str :='select ORM_USER_Document.patch_file, count(ORM_USER_Document.email)
                        from ORM_USER_Document ';

        -- optional part where
            if patch_file is not null then
             query_str:= query_str||' where trim(ORM_USER_Document.patch_file) = trim('''||Document_name||''') ';
            end if;
        -- end optional part

        query_str := query_str||' group by ORM_USER_Document.Document_name';



        OPEN Document_cursor FOR query_str;
        LOOP
            FETCH Document_cursor into cursor_data;
            exit when (Document_cursor %NOTFOUND);

            PIPE ROW (cursor_data);

        END LOOP;


    END GetDocumentData;

END orm_user_Document;
