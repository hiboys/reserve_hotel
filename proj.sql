
use hotel_db;

CREATE TABLE guest(
  gid int(10) unsigned NOT NULL auto_increment,
  firstname varchar(256) NOT NULL,
  lastname varchar(256) NOT NULL,
  PRIMARY KEY  (gid)
) ;

create table location(
  lid int(10) unsigned NOT NULL auto_increment,
  city varchar(256) not null,
  province varchar(256) not null,
  PRIMARY KEY  (lid)
);

create table hotel(
  hid int(10) unsigned NOT NULL auto_increment,
  address_id int unsigned not null,
  description text not null,
  hotelname varchar(256) not null,
  stars int unsigned not null,
  PRIMARY KEY  (hid),
  foreign key (address_id) REFERENCES location(lid)
);

create table room(
  rid int(10) unsigned NOT NULL auto_increment,
  hotel_id int unsigned not null,
  room_type int not null,
  price float not null,
  check_in date, 
  check_out date,
  PRIMARY KEY  (rid),
  foreign key (hotel_id) REFERENCES hotel(hid)
);
