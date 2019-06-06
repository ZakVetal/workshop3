create or replace PACKAGE search IS


    TYPE search IS RECORD(
        channel_name_ CHANNEL.channel_name%TYPE,
        subscribers_count INTEGER
    );


    TYPE tblres IS TABLE OF skill_data;

    FUNCTION search_channel (m1 INTEGER default null,m2 INTEGER default null)
        RETURN tblres
        PIPELINED;

END orm_user_skills;