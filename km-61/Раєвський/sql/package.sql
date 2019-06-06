CREATE OR REPLACE PACKAGE orm_worker_assignment IS
    TYPE job_data IS RECORD(
        worker_name WORKER.worker_name%TYPE,
        worker_surname WORKER.worker_surname%TYPE,
        assignment_name ASSIGNMENT.ASSIGNMENT_NAME%TYPE,
        assignment_time ASSIGNMENT.assignment_time%TYPE,
        assignment_date WORKER_ASSIGNMENT.wa_assignment_date%TYPE,
        assignment_complete_time WORKER_ASSIGNMENT.wa_complete_time%TYPE
    );

    TYPE job_table IS TABLE OF job_data;

    FUNCTION GetJob (worker_surname WORKER.worker_surname%TYPE default null, assignment_name ASSIGNMENT.ASSIGNMENT_NAME%TYPE default null)
        RETURN job_table
        PIPELINED;

END orm_worker_assignment;


CREATE OR REPLACE PACKAGE BODY orm_worker_assignment IS
    FUNCTION GetJob (worker_surname WORKER.worker_surname%TYPE default null, assignment_name ASSIGNMENT.ASSIGNMENT_NAME%TYPE default null)
    RETURN job_table
    PIPELINED
    IS
        TYPE worker_cursor_type IS REF CURSOR;
        worker_cursor  worker_cursor_type;

        cursor_data job_data;
        query_str varchar2(1000);

    begin
        query_str :='select worker.worker_name, worker.worker_surname, assignment.assignment_name, assignment.assignment_time, worker_assignment.wa_assignment_date, worker_assignment.wa_complete_time
        from worker 
        inner join worker_assignment on worker.worker_id = worker_assignment.wa_worker_id_fk 
        inner join assignment on assignment.assignment_id = worker_assignment.wa_assignment_id_fk';
        
        
        -- optional part where
        if worker_surname is not null or assignment_name is not null then
            query_str := query_str || ' where ';
        end if;
            
            if worker_surname is not null then
             query_str := query_str ||'trim(worker.worker_surname) = trim('''||worker_surname||''')';
            end if;
            
            if assignment_name is not null and worker_surname is not null then
             query_str := query_str || ' and ';
            end if;
            
            if assignment_name is not null then
             query_str := query_str ||'trim(assignment.assignment_name) = trim('''||assignment_name||''')';
            end if;
        -- end optional part

        query_str := query_str||' order by worker.worker_name';



        OPEN worker_cursor FOR query_str;
        LOOP
            FETCH worker_cursor into cursor_data;
            exit when (worker_cursor %NOTFOUND);

            PIPE ROW (cursor_data);

        END LOOP;


    END GetJob;

END orm_worker_assignment;