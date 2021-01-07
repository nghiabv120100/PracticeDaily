Create database NNLTTT;

use NNLTTT;

Create table Word
(
	id int auto_increment,
    vocabulary varchar(255),
    means nvarchar(255),
    image nvarchar(255), -- lưu link đến vị trí để ảnh
    level_box int, -- Tuơng ứng với vị trí ở hộp 0: Source, 1: Box1, 2:Box2....
	part_of_speech varchar(50),
    eg nvarchar(1000),  
    primary key(id)
);


create table review
(
	id_Word int,
    status int default -1,
    date_practice date default(curdate()),
    Foreign Key(id_Word) references Word(id),
    Primary Key(id_Word,date_practice)
);