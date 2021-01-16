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
 Select * from word;
Select * from review;
delete from word where id > 0;
INSERT INTO review VALUES (1, 0, curdate());
INSERT INTO word VALUES (0,"white", "trắng", null, 0, "noun");
INSERT INTO word VALUES (0,"black", "đen", null, 0, "noun");
INSERT INTO word VALUES (0,"yellow", "vàng", null, 0, "noun");
INSERT INTO word VALUES (0,"blue", "xanh dương", null, 0, "noun");
INSERT INTO word VALUES (0,"green", "xanh lá", null, 0, "noun");
INSERT INTO word VALUES (0,"gray", "xám", null, 0, "noun");
INSERT INTO word VALUES (0,"brown", "nâu", null, 0, "noun");
INSERT INTO word VALUES (0,"orange", "cam", null, 0, "noun");
INSERT INTO word VALUES (0,"pink", "hồng", null, 0, "noun");
INSERT INTO word VALUES (0,"purple", "tím", null, 0, "noun");
INSERT INTO word VALUES (0,"red", "đỏ", null, 0, "noun");
INSERT INTO word VALUES (0,"silver", "bạc", null, 0, "noun");

INSERT INTO word VALUES (0,"employee", "nhân viên", null, 0, "noun");
INSERT INTO word VALUES (0,"manager", "quản lý", null, 0, "noun");
INSERT INTO word VALUES (0,"salary", "lương", null, 0, "noun");
INSERT INTO word VALUES (0,"interview", "phỏng vấn", null, 0, "noun");
INSERT INTO word VALUES (0,"company", "công ty", null, 0, "noun");
INSERT INTO word VALUES (0,"department", "phòng ban", null, 0, "noun");
INSERT INTO word VALUES (0,"customer", "khách hàng", null, 0, "noun");
INSERT INTO word VALUES (0,"project", "dự án", null, 0, "noun");
INSERT INTO word VALUES (0,"office", "văn phòng", null, 0, "noun");
INSERT INTO word VALUES (0,"colleague", "đồng nghiệp", null, 0, "noun");
INSERT INTO word VALUES (0,"presentation", "bài thuyết trình", null, 0, "noun");
INSERT INTO word VALUES (0,"document", "tài liệu", null, 0, "noun");

INSERT INTO word VALUES (0,"banana", "chuối", null, 0, "noun");
INSERT INTO word VALUES (0,"mango", "xoài", null, 0, "noun");
INSERT INTO word VALUES (0,"coconut", "dừa", null, 0, "noun");
INSERT INTO word VALUES (0,"watermelon", "dưa hấu", null, 0, "noun");
INSERT INTO word VALUES (0,"durian", "sầu riêng", null, 0, "noun");
INSERT INTO word VALUES (0,"lemon", "chanh", null, 0, "noun");
INSERT INTO word VALUES (0,"plum", "mận", null, 0, "noun");
INSERT INTO word VALUES (0,"pear", "lê", null, 0, "noun");
INSERT INTO word VALUES (0,"strawberry", "dâu tây", null, 0, "noun");
INSERT INTO word VALUES (0,"pineapple", "dứa", null, 0, "noun");
INSERT INTO word VALUES (0,"grape", "nho", null, 0, "noun");
INSERT INTO word VALUES (0,"apple", "táo", null, 0, "noun");
INSERT INTO word VALUES (0,"tamarind", "me", null, 0, "noun");
INSERT INTO word VALUES (0,"star fruit", "khế", null, 0, "noun");
INSERT INTO word VALUES (0,"dragon fruit", "thanh long", null, 0, "noun");
INSERT INTO word VALUES (0,"pomegranate", "lựu", null, 0, "noun");

#############################################################################

-- Recruitment (level_box=-1
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('interviewer','người phỏng vấn','interviewer.png',-1,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('candidate','ứng cử viên','candidate.png',-1,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('position','chức vụ','position.png',-1,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('specialty','chuyên môn','specialty.png',-1,'Adv');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('vacancies','vị trí tuyển dụng','vacancies.png',-1,'Noun');
-- --------------------------
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('training','đào tạo','training.png',-1,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('qualification','trình độ chuyên môn','qualification.png',-1,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('application','hồ sơ','application.png',-1,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('cv','sơ yếu lý lịch','cv.png',-1,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('test','kiểm tra','test.png',-1,'Noun');
-- -----------------------------
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('manager','giám đốc','manager.png',-1,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('employee','nhân viên','employee.png',-1,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('experience','kinh nghiệm','experience.png',-1,'Adj');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('selection','sự lựa chọn','selection.png',-1,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('project','dự án','project.png',-1,'Adj');

-- ==========================================================================
-- Workspace(level_box = -2)
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('workplace','nơi làm việc','workplace.png',-2,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('company','công ty','company.png',-2,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('restaurant','nhà hàng','restaurant.png',-2,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('hospital','bệnh viện','hospital.png',-2,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('hotel','khách sạn','hotel.png',-2,'Noun');
-- --------------------------
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('facilities','cơ sở vật chất','facilities.png',-2,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('furnish','sự tiện nghi','furnish.png',-2,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('equipment','trang thiết bị','equipment.png',-2,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('park','công viên','park.png',-2,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('zoo','vườn bách thú','zoo.png',-2,'Noun');
-- -----------------------------
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('office','văn phòng','office.png',-2,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('school','trường học','school.png',-2,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('airport','sân bay','airport.png',-2,'Adj');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('shop','cửa tiệm','shop.png',-2,'Noun');
insert into word(vocabulary,means,image,level_box,part_of_speech)
values('museum','viện bảo tàng','museum.png',-2,'Noun');


#Bussiness(level_box=-3)

Insert INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("account", "tài khoản", "account.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("advertisement", "quảng cáo", "advertisement.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("company", "công ty", "company.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("profit", "lợi nhuận", "profit.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("tax", "thuế", "tax.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("invest", "đầu tư", "invest.png", -3, "verb");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("loan", "khoản vay", "loan.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("cash", "tiền mặt", "cash.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("colleague", "đồng nghiệp", "colleague.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("receipt", "biên nhận", "receipt.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("market", "thị trường", "market.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("financial", "tài chính", "financial.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("secretary", "thư ký", "secretary.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("corporation", "tập đoàn", "corporation.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("stock", "cổ phiếu", "stock.png", -3, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("salary", "lương", "salary.png", -3, "noun");



#Shopping(level_box=-4)
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("shop", "cửa hàng", "shop.png", -4, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("price", "giá", "price.png", -4, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("brand", "thương hiệu", "brand.png", -4, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("discount", "giảm giá", "discount.png", -4, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("mall", "trung tâm mua sắm", "mall.png", -4, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("expensive", "đắt", "expensive.png", -4, "adj");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("cheap", "rẻ", "cheap.png", -4, "adj");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("pay", "thanh toán", "pay.png", -4, "verb");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("promotion", "khuyến mãi", "promotion.png", -4, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("jewelry", "trang sức", "jewelry.png", -4, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("counter", "quầy tính tiền", "counter.png", -4, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("shirt", "áo", "shirt.png", -4, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("jeans", "quần jeans", "jeans.png", -4, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("shoes", "giày", "shoes.png", -4, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("bill", "hoá đơn", "bill.png", -4, "noun");


#Travel(level_box =-5)

INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("vehicle", "phương tiện", "vehicle.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("tourist", "du khách", "tourist.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("guide", "hướng dẫn", "guide.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("luggage", "hành lý", "luggage.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("trip", "chuyến đi", "trip.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("book", "đặt chỗ", "book.png", -5, "verb");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("transfer", "vận chuyển ", "transfer.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("schedule", "lịch trình", "schedule.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("destination", "điểm đến", "destination.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("ticket", "vé", "ticket.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("flight", "chuyến bay", "flight.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("passenger", "hành khách", "passenger.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("railway", "đường sắt", "railway.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("landscape", "phong cảnh", "landscape.png", -5, "noun");
INSERT INTO word(vocabulary,means,image,level_box,part_of_speech) VALUES ("highway", "đường cao tốc", "highway.png", -5, "noun");