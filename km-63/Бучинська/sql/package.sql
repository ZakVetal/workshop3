create or replace package edit_u is
  procedure new_user(

                            user_phoneIN in TUSER.user_phone%TYPE,
                            user_nameIN in TUSER.user_name%TYPE,
                            user_surnameIN in TUSER.user_surname%TYPE,
                            user_genderIN in TUSER.user_gender%TYPE,
                            status out varchar2


                        );
     procedure update_user(

                            user_phoneIN in TUSER.user_phone%TYPE,
                            user_nameIN in TUSER.user_name%TYPE,
                            user_surnameIN in TUSER.user_surname%TYPE,
                            user_genderIN in TUSER.user_gender%TYPE,
                            status out varchar2

                        );
     procedure del_user(

                            user_phoneIN in TUSER.user_phone%TYPE,
                            status out varchar2


                        );
      procedure new_channel(

                            channel_urlIN in CHANNEL.channel_url%TYPE,
                            channel_nameIN in CHANNEL.channel_name%TYPE,
                            status out varchar2


                        );
     procedure update_channel(

                            channel_urlIN in CHANNEL.channel_url%TYPE,
                            channel_nameIN in CHANNEL.channel_name%TYPE,
                            status out varchar2

                        );
     procedure del_channel(

                            channel_urlIN in CHANNEL.channel_url%TYPE,
                            status out varchar2


                        );
      procedure new_subscription(

                            user_phoneIN in SUBSC.user_phone%TYPE,
                            channel_urlIN in SUBSC.channel_url%TYPE,
                            subscription_dateIN in SUBSC.subscription_date%TYPE,

                            status out varchar2


                        );

     procedure del_subscription(
                            channel_urlIN in SUBSC.channel_url%TYPE,
                            user_phoneIN in SUBSC.user_phone%TYPE,
                            status out varchar2


                        );




            end edit_u