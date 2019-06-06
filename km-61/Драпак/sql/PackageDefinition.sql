CREATE OR REPLACE PACKAGE user_actions AS
    TYPE name_list_number IS RECORD(
        user_name "User".full_name%TYPE,
        list_name TODOList."name"%TYPE,
        list_date TODOList."date"%TYPE,
        actions_number NUMBER(8)
    );
    TYPE name_number_tbl IS TABLE OF name_list_number;
    TYPE ref_cur_type IS REF CURSOR;
    FUNCTION get_actions_number(user_name "User".full_name%TYPE DEFAULT NULL,
    start_date DATE DEFAULT NULL, end_date DATE DEFAULT NULL) RETURN name_number_tbl PIPELINED;
END user_actions;

CREATE OR REPLACE PACKAGE BODY user_actions AS
    FUNCTION get_actions_number(user_name "User".full_name%TYPE DEFAULT NULL,
    start_date DATE DEFAULT NULL, end_date DATE DEFAULT NULL) RETURN name_number_tbl PIPELINED IS
        ref_cur ref_cur_type;
        new_tbl_row name_list_number;
        query_str VARCHAR2(1023);
        where_identifier NUMBER(1) DEFAULT 0;
    BEGIN
        query_str := 'SELECT "User".full_name, TODOList."name", TODOList."date", COUNT(Action.TIME_OPEN) ' ||
            'FROM "User" JOIN TODOList ON "User".full_name = TODOList.full_name ' ||
            'JOIN Action ON TODOList."date" = Action."date" AND TODOList."name" = Action."name" ' || 'WHERE ';
        IF user_name IS NOT NULL THEN
            query_str := query_str || '"User".full_name = :user_name AND ';
        ELSE
            query_str := query_str || ':user_name IS NULL AND';
        END IF;
        IF start_date IS NOT NULL AND end_date IS NOT NULL THEN
            query_str := query_str || 'Action.time_open BETWEEN :start_date AND :end_date AND ' ||
            'Action.time_close BETWEEN :start_date AND :end_date ';
        ELSE
            query_str := query_str || ':start_date IS NULL AND :end_date IS NULL AND ' ||
            ':start_date IS NULL AND :end_date IS NULL ';
        END IF;
        query_str := query_str  || 'GROUP BY "User".full_name, TODOList."name", TODOList."date"';
        OPEN ref_cur FOR query_str USING user_name, start_date, end_date, start_date, end_date;
        LOOP
            FETCH ref_cur INTO new_tbl_row;
            EXIT WHEN ref_cur%NOTFOUND;
            PIPE ROW(new_tbl_row);
        END LOOP;
        CLOSE ref_cur;
        RETURN;
    END get_actions_number;
END user_actions;