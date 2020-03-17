CREATE TABLE customerTable(
	customerId SERIAL PRIMARY KEY,
	customerName VARCHAR(30),
	customerEmail VARCHAR(50),
	DistanceCovered NUMERIC(10)
);
INSERT INTO customerTable
	(customerName,customerEmail,DistanceCovered)
VALUES
	('Bobby Charlton','bobbycharl@ymail.com',3000),
	('Dennis Law','dennisthemenance@outlook.com',2000),
	('George Best','bestisbest@quixote.com',10000),
	('Roy Keane','keanoroy@hotmail.com',2000),
	('Paul Scholes','scholsey@gmail.com',12000),
	('Ryan Giggs','ryangiggs@gmail.com',15000),
	('Nemanja Vidic','vidicnemanja@gmail.com',10000);


CREATE TABLE driverTable(
	driverId SERIAL PRIMARY KEY,
	driverName VARCHAR(30),
	vehicleName VARCHAR(50),
	totalDistance NUMERIC(10)
);
INSERT INTO driverTable
	(driverName,vehicleName,totalDistance)
VALUES
	('Sir Matt Busby','Mercedes',30000),
	('Jimmy Murphy','Ford',25000),
	('Sir Alex Ferguson','Aston Martin',100000),
	('David McGill','Toyota',20000);

CREATE TABLE locationTable(
	locationId SERIAL PRIMARY KEY,
	addressloc VARCHAR(30),
	city VARCHAR(30),
	country VARCHAR(30),
	region VARCHAR(30)
);

INSERT INTO locationtable
	(addressloc, city, country, region)
VALUES
	('Stretford','Manchester','Great Britain','Europe'),
	('Tottenham','London','Great Britain','Europe'),
	('Carlsyle','Edinburgh','Scotland','Europe'),
	('Abaroska','Dakota','United States of America','America'),
	('Tianmenn','Beijing','China','Asia');


