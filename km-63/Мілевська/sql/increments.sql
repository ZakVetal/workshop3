CREATE OR REPLACE TRIGGER TRG_INSERT_ORM_USER
BEFORE INSERT ON "SYSTEM"."ORM_USER"
FOR EACH ROW
BEGIN
  :NEW.user_id:="ORM_USER_ID".NEXTVAL;
END;

CREATE OR REPLACE TRIGGER TRG_INSERT_ORM_EVENT
BEFORE INSERT ON "SYSTEM"."ORM_EVENT"
FOR EACH ROW
BEGIN
  :NEW.event_id:="ORM_EVENT_ID".NEXTVAL;
END;
