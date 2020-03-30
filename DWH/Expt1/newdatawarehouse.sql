CREATE TABLE spectator(
	spectator_id SERIAL PRIMARY KEY,
	spectator_name VARCHAR(30),
	status VARCHAR(50),
	phone_number NUMERIC(10),
    address VARCHAR(100)
);

INSERT INTO spectator(spectator_name,status,phone_number,address)VALUES
('Fiyori Elias','student',6434732623,'90,Reisenoir 45710 Madridejos'),
('Ulrike Reiniger','student',03784688370,'120,Via Scuderlando
64010-Civitella Del Tronto TE'),
('Guilherme Cunha Cavalcanti','teacher',0892585793,'41 Daly Terrace CURRAMBINE WA 6028'),
('Galina Kudryashova','teacher',7063664327,'99 Withers Close, ALLGREAVE,SK11 5HH'),
('Isao Toyota','student',78310125,'107 Rue Echikh Mohamed Abbes
6172 EL BARRAMA');

CREATE TABLE datetable(
	date_id SERIAL PRIMARY KEY,
	day_entry VARCHAR(50),
	month_entry NUMERIC(10),
    quarter_entry NUMERIC(10),
    year_entry NUMERIC(10)
);

INSERT INTO datetable
	(day_entry, month_entry, quarter_entry, year_entry)
VALUES
	('Monday',03,2,2018),
	('Tuesday',10,3,2019),
	('Wednesday',09,4,2020),
	('Friday',04,1,2018),
    ('Sunday',11,2,2017);

CREATE TABLE datetable(
	date_id SERIAL PRIMARY KEY,
	day_entry VARCHAR(50),
	month_entry NUMERIC(10),
    quarter_entry NUMERIC(10),
    year_entry NUMERIC(10)
);

INSERT INTO datetable
	(day_entry, month_entry, quarter_entry, year_entry)
VALUES
	('Monday',03,2,2018),
	('Tuesday',10,3,2019),
	('Wednesday',09,4,2020),
	('Friday',04,1,2018),
    ('Sunday',11,2,2017);
