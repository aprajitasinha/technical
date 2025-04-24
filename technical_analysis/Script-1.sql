--CREATE TABLE candleanalyticsdb (
--    stock_id SERIAL PRIMARY KEY,
--    symbol TEXT NOT NULL,
--    company_name TEXT NOT NULL,
--    market TEXT NOT NULL,
--    created_at TIMESTAMP NOT NULL DEFAULT NOW()
--);

--SELECT current_database();

--Find the Current Schema:
--SELECT current_schema();
--
--List All Tables in the Current Schema:
--SELECT table_schema, table_name
--FROM information_schema.tables
--WHERE table_type = 'BASE TABLE'
--  AND table_name = 'stock_data';


--ALTER TABLE candleanalyticsdb RENAME TO stock_metadata;

--SELECT *
--FROM information_schema.tables
--WHERE table_name = 'stock_data.candle_data';

--SELECT column_name, data_type, is_nullable, column_default
--FROM information_schema.columns
--WHERE table_name = 'stock_metadata';

--DROP TABLE stock_data.candle_data;
--drop schema stock_data cascade;

--created schema
--CREATE SCHEMA stock_data;

--created table
--CREATE TABLE stock_data.candle_data_id (
--    stock_id SERIAL PRIMARY KEY,
--    symbol TEXT NOT NULL,
--    company_name TEXT NOT NULL,
--    market TEXT  NULL,
--    created_at TIMESTAMP NOT NULL DEFAULT NOW()
--);

--to see all schema
--SELECT schema_name 
--FROM information_schema.schemata;

--to see table inside schema
--SELECT table_name
--FROM information_schema.tables
--WHERE table_schema = 'stock_data';

--to see schema
--SELECT table_schema
--FROM information_schema.tables
--WHERE table_name = 'candle_data_id';

--to see information inside all coulms
--SELECT column_name, data_type, is_nullable, column_default
--FROM information_schema.columns
--WHERE table_schema = 'stock_data' AND table_name = 'candle_data_id';



--SELECT sequence_name
--FROM information_schema.sequences
--WHERE sequence_schema = 'stock_data' AND sequence_name LIKE 'candle_data_stock_id_seq';

--#to check schemas
--SELECT schema_name
--FROM information_schema.schemata;

--DROP schema ADANIPORTS cascade ;

--DROP SCHEMA IF EXISTS CIPLA CASCADE;
--DROP SCHEMA IF EXISTS ADANIPORTS CASCADE;
--DROP SCHEMA IF EXISTS ADANIENT CASCADE;
--DROP SCHEMA IF EXISTS ADANIGREEN CASCADE;
--DROP SCHEMA IF EXISTS ADANIPOWER CASCADE;
--DROP SCHEMA IF EXISTS AMBUJACEM CASCADE;
--DROP SCHEMA IF EXISTS APOLLOHOSP CASCADE;

--SELECT * FROM "UPL"."candle_1w";
--SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'ADANIENT';

--SELECT table_schema 
--FROM information_schema.] 
--WHERE table_schema = 'UPL';

--INSERT INTO "UPL"."candle_1w" (timestamp, open, high, low, close, volume)
--VALUES ('2025-04-24 09:15:00', 679.55, 684.45, 675.45, 682.55, 1930613)
--ON CONFLICT (timestamp) DO NOTHING;
--SELECT table_name
--FROM information_schema.tables
--WHERE table_schema = 'UPL';

--GRANT ALL PRIVILEGES ON SCHEMA "UPL" TO aryanpatel;
--CREATE TABLE IF NOT EXISTS "UPL"."candle_3m" (
--    timestamp TIMESTAMP PRIMARY KEY,
--    open NUMERIC,
--    high NUMERIC,
--    low NUMERIC,
--    close NUMERIC,
--    volume NUMERIC
--);
--SELECT table_name
--FROM information_schema.tables
--WHERE table_schema = 'UPL';
--INSERT INTO "UPL"."candle_1w" (timestamp, open, high, low, close, volume)
--VALUES ('2025-04-24 09:15:00', 679.55, 684.45, 675.45, 682.55, 1930613)
--ON CONFLICT (timestamp) DO NOTHING;




--CREATE TABLE Persons (
--  PersonID int NOT NULL PRIMARY KEY,
--  LastName varchar(255) NOT NULL,
--  FirstName varchar(255),
--  Age int
--);
--INSERT INTO Persons (PersonID, LastName, FirstName, Age) VALUES
--  (1,'Thakur', 'Aditya', 22),
--  (2, 'Kumar', 'Shubham', 21);

--CREATE TABLE Persons ( 
--  PersonID int,
--  LastName varchar(255) NOT NULL,
--  FirstName varchar(255),  Age int);
--select * from Persons;
--drop table Persons;

--#This query will add primary key to ‘Persons’ table

--ALTER TABLE Persons
--ADD CONSTRAINT PK_Person PRIMARY KEY (PersonID);
--GRANT ALL PRIVILEGES ON DATABASE candleanalyticsdb TO aryanpatel;
--drop table stocks;
SELECT * FROM "ADANIGREEN"."candle_1m";
