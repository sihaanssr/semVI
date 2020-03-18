CREATE TABLE dimproduct(
	pid VARCHAR(30) PRIMARY KEY,
	pkey VARCHAR(30),
	pname VARCHAR(50),
	unitprice NUMERIC(10),
    category VARCHAR(30),
);
INSERT INTO dimproduct
	(pid, pkey, pname, unitprice, category)
VALUES
	('1','1001','lg',3000,'phone'),
	('2','1001','lg',2000,'washingmachine'),
	('3','1002','samsung',10000,'phone'),
	('4','1003','apple',2000,'laptop'),
	('5','1004','nokia',12000,'phone');

CREATE TABLE dimtimetable(
	tid VARCHAR(30) PRIMARY KEY,
	tkey VARCHAR(30),
	day VARCHAR(50),
	month NUMERIC(10),
    quarter NUMERIC(10),
    year NUMERIC(10),

);
INSERT INTO dimtimetable
	(tid, tkey, day, month, quarter, year)
VALUES
	('12','1111','Monday',3,2,2018),
	('34','2222','Tuesday',2,3,2019),
	('56','3333','Wednesday',1,4,2020),
	('78','4444','Friday',4,1,2018),
    ('90','5555','Sunday',11,2,2017);

CREATE TABLE dimstore(
	sid VARCHAR(30) PRIMARY KEY,
    skey VARCHAR(30),
	sname VARCHAR(30),
	city VARCHAR(30),
    state VARCHAR(30),
	country VARCHAR(30),
	region VARCHAR(30)
);

INSERT INTO dimstore
	(sid, skey, sname, city, state, county, region)
VALUES
	('11','1234','Stretford','Manchester','Great Britain','Great Britain','Europe'),
	('22','2345','Tottenham','London','Great Britain','Great Britain','Europe'),
	('33','3456','Carlsyle','Edinburgh','Scotland','Scotland','Europe'),
	('44','4567','Abaroska','Dakota','California','United States of America','America'),
	('55','5678','Tianmenn','Beijing','Wuhan','China','Asia');


CREATE TABLE factsales(
    pid VARCHAR(30) REFERENCES product(pid),
    sid VARCHAR(30) REFERENCES store(sid),
    tid VARCHAR(30) REFERENCES timetable(tid),
    units_sold NUMERIC(30),
    total_sales NUMERIC(30)
);
INSERT INTO factsales(pid, sid, tid, units_sold, total_sales)
VALUES
    ('1','11','12',1000,20000),
    ('2','11','34',2000,40000),
    ('3','22','56',3000,60000),
    ('4','33','78',4000,70000),
    ('5','44','90',5000,90000);
