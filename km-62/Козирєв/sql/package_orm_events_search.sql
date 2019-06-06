CREATE OR REPLACE PACKAGE orm_searcher IS

    TYPE event_container IS RECORD(
        event_date ORMEVENT.event_date%TYPE,
        event_description ORMEVENT.event_description%TYPE,
        event_state ORMEVENT.event_state%TYPE,
        priority_description ORMPRIORITY.priority_description%TYPE
    );

    TYPE pointer_to_event_container IS TABLE OF event_container;

    FUNCTION GetRequiredEvents ()
        RETURN pointer_to_event_container
        PIPELINED;

END orm_searcher;




CREATE OR REPLACE PACKAGE BODY orm_searcher IS

    FUNCTION GetRequiredEvents (skill_name ORM_SKILL.SKILL_NAME%TYPE default null)
    RETURN pointer_to_event_container
    PIPELINED
    IS

        TYPE event_container_cursor_type IS REF CURSOR;
        event_cursor  event_container_cursor_type;

        event_cursor_data event_container;
        query_str varchar2(1000);

    begin

        query_str :='select ORM_USER_SKILL.skill_name, count(ORM_USER_SKILL.user_id) from ORM_USER_SKILL where trim(ORM_USER_SKILL.skill_name) = trim('''||skill_name||''') and trim(ORM_USER_SKILL.skill_name) = trim('''||skill_name||''') and trim(ORM_USER_SKILL.skill_name) = trim('''||skill_name||''') and trim(ORM_USER_SKILL.skill_name) = trim('''||skill_name||''')';

        OPEN event_cursor FOR query_str;
        LOOP
            FETCH event_cursor into event_cursor_data;
            exit when (event_cursor %NOTFOUND);

            PIPE ROW (event_cursor_data);

        END LOOP;


    END GetRequiredEvents;

END orm_searcher;