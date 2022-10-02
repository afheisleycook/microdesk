create table IF NOT EXISTS `users` (
    users_id bigint(20) primary key auto_increment not null,
    users_name text not null unique,
    users_password text not null,
    user_role = text not null default "basic",

    
)

insert into `users` (null, "admin", "P@ssw0rd", "admin")