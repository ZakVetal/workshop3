/*==============================================================*/
/* DBMS name:      ORACLE Version 11g                           */
/* Created on:     06.06.2019 5:31:32                           */
/*==============================================================*/


alter table "WORKER_ASSIGNMENT"
   drop constraint FK_WORKER_A_ASSIGNMEN_ASSIGNME;

alter table "WORKER_ASSIGNMENT"
   drop constraint FK_WORKER_A_WORKER_HA_WORKER;

drop table "ASSIGNMENT" cascade constraints;

drop table "WORKER" cascade constraints;

drop table "WORKER_ASSIGNMENT" cascade constraints;

/*==============================================================*/
/* Table: "assignment"                                          */
/*==============================================================*/
create table "ASSIGNMENT" 
(
   "ASSIGNMENT_ID"      INTEGER              not null,
   "ASSIGNMENT_NAME"    VARCHAR2(30)         not null,
   "ASSIGNMENT_DESCRIPTION" VARCHAR2(2000)       not null,
   "ASSIGNMENT_TIME"    DATE                 not null,
   constraint PK_ASSIGNMENT primary key ("ASSIGNMENT_ID")
);

/*==============================================================*/
/* Table: "worker"                                              */
/*==============================================================*/
create table "WORKER" 
(
   "WORKER_ID"          INTEGER              NOT NULL,
   "WORKER_NAME"        VARCHAR2(30)         NOT NULL,
   "WORKER_SURNAME"     VARCHAR2(30)         NOT NULL,
   "WORKER_PATRONYMIC"  VARCHAR2(30),
   "WORKER_BIRTH_DATE"  DATE                 NOT NULL,
   "WORKER_JOB_TITLE"   VARCHAR2(30)         NOT NULL,
   constraint PK_WORKER primary key ("WORKER_ID")
);

/*==============================================================*/
/* Table: "worker_assignment"                                   */
/*==============================================================*/
create table "WORKER_ASSIGNMENT" 
(
   "WA_WORKER_ID_FK"    INTEGER              not null,
   "WA_ASSIGNMENT_ID_FK" INTEGER              not null,
   "WA_ASSIGNMENT_DATE" DATE                 not null,
   "WA_COMPLETE_TIME"   DATE,                 
   constraint PK_WORKER_ASSIGNMENT primary key ("WA_WORKER_ID_FK", "WA_ASSIGNMENT_ID_FK")
);

alter table "WORKER_ASSIGNMENT"
   add constraint ASSIGNMENT_ID_FK foreign key ("WA_ASSIGNMENT_ID_FK")
      references "ASSIGNMENT" ("ASSIGNMENT_ID");

alter table "WORKER_ASSIGNMENT"
   add constraint WORKER_ID_FK foreign key ("WA_WORKER_ID_FK")
      references "WORKER" ("WORKER_ID");
      
CREATE SEQUENCE SEQ_WORKER_ID
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1;
    
CREATE OR REPLACE TRIGGER TRG_INSERT_WORKER
BEFORE INSERT ON WORKER
FOR EACH ROW
BEGIN
    :NEW.worker_id:=SEQ_WORKER_ID.NEXTVAL;
END;


CREATE SEQUENCE SEQ_ASSIGNMENT_ID
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1;
    
CREATE OR REPLACE TRIGGER TRG_INSERT_ASSIGNMENT
BEFORE INSERT ON ASSIGNMENT
FOR EACH ROW
BEGIN
    :NEW.assignment_id:=SEQ_ASSIGNMENT_ID.NEXTVAL;
END;

