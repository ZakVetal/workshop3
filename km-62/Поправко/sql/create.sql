create table user(username varchar(20),user_email varchar(13),user_id number(15));
alter table user add constraint pk_user primary  key(number_of_daybook);

create table history_of_views(time_of_view date,like boolean);
alter table history_of_views add constraint pk_user primary  key(time_of_view);

create table news( username varchar(20),news_title varchar(20),news_source varchar(20), news_author varchar(20));
alter table news add constraint pk_user primary  key(,time_of_view);
alter table news add constraint
fk1 foreign key referenses history_of_views(time_of_view);
alter table news add constraint
fk2 foreign key referenses news(news_title, username);