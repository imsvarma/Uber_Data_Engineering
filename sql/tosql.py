# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 16:59:41 2025

@author: imani
"""


import pandas as pd
import datetime
from sqlalchemy import *
from db_connect import engine
from ETL_uber import datetime_dim, passenger_count_dim, rate_code_dim, pickup_location_dim, dropoff_location_dim, payment_type_dim, trip_distance_dim, fact_table
from db_connect import metadata, engine

create_table_sql = """

CREATE TABLE dbo.datetime_dim (
    datetime_id INT NOT NULL PRIMARY KEY,
    tpep_pickup_datetime DATETIME,
    pick_hour INT,
    pick_day INT,
    pick_month INT,
    pick_year INT,
    pick_weekday INT,
    tpep_dropoff_datetime DATETIME,
    drop_hour INT,
    drop_day INT,
    drop_month INT,
    drop_year INT,
    drop_weekday INT
);

CREATE TABLE dbo.passenger_count_dim (
    passenger_count_id INT NOT NULL PRIMARY KEY,
    passenger_count INT
);

CREATE TABLE dbo.rate_code_dim (
    rate_code_id INT NOT NULL PRIMARY KEY,
    RatecodeID INT,
    rate_code_name VARCHAR(50)
);

CREATE TABLE dbo.pickup_location_dim (
    pickup_location_id INT NOT NULL PRIMARY KEY,
    pickup_latitude FLOAT,
    pickup_longitude FLOAT
);

CREATE TABLE dbo.dropoff_location_dim (
    dropoff_location_id INT NOT NULL PRIMARY KEY,
    dropoff_latitude FLOAT,
    dropoff_longitude FLOAT
);

CREATE TABLE dbo.payment_type_dim (
    payment_type_id INT NOT NULL PRIMARY KEY,
    payment_type INT,
    payment_type_name VARCHAR(50)
);

CREATE TABLE dbo.trip_distance_dim (
    trip_distance_id INT NOT NULL PRIMARY KEY,
    trip_distance FLOAT
);

CREATE TABLE dbo.fact_table (
    trip_id INT NOT NULL PRIMARY KEY,
    VendorID INT,
    datetime_id INT,
    passenger_count_id INT,
    trip_distance_id INT,
    rate_code_id INT,
    store_and_fwd_flag VARCHAR(10),
    pickup_location_id INT,
    dropoff_location_id INT,
    payment_type_id INT,
    fare_amount DECIMAL(10, 2),
    extra DECIMAL(10, 2),
    mta_tax DECIMAL(10, 2),
    tip_amount DECIMAL(10, 2),
    tolls_amount DECIMAL(10, 2),
    improvement_surcharge DECIMAL(10, 2),
    total_amount DECIMAL(10, 2)
);
"""

with engine.connect() as conn:
    conn.execute(text(create_table_sql))
    print("Tables created")

datetime_dim.to_sql('datetime_dim', con=engine, if_exists='append', index=False)
passenger_count_dim.to_sql('passenger_count_dim', con=engine, if_exists='append', index=False)
rate_code_dim.to_sql('rate_code_dim', con=engine, if_exists='append', index=False)
pickup_location_dim.to_sql('pickup_location_dim', con=engine, if_exists='append', index=False)
dropoff_location_dim.to_sql('dropoff_location_dim', con=engine, if_exists='append', index=False)
payment_type_dim.to_sql('payment_type_dim', con=engine, if_exists='append', index=False)
trip_distance_dim.to_sql('trip_distance_dim', con=engine, if_exists='append', index=False)
fact_table.to_sql('fact_table', con=engine, if_exists='append', index=False)

print("Data inserted successfully")











