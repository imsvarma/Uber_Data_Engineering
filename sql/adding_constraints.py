# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 13:11:53 2025

@author: imani
"""
from ETL_uber import datetime_dim, passenger_count_dim, rate_code_dim, pickup_location_dim, dropoff_location_dim, payment_type_dim, trip_distance_dim, fact_table
from db_connect import metadata, engine
from db_connect import engine
from sqlalchemy import create_engine, text

# 4. Add PK and FK constraints
add_constraints_sql = """
ALTER TABLE dbo.datetime_dim
ADD CONSTRAINT PK_datetime_dim PRIMARY KEY (datetime_id);

ALTER TABLE dbo.passenger_count_dim
ADD CONSTRAINT PK_passenger_count_dim PRIMARY KEY (passenger_count_id);

ALTER TABLE dbo.rate_code_dim
ADD CONSTRAINT PK_rate_code_dim PRIMARY KEY (rate_code_id);

ALTER TABLE dbo.pickup_location_dim
ADD CONSTRAINT PK_pickup_location_dim PRIMARY KEY (pickup_location_id);

ALTER TABLE dbo.dropoff_location_dim
ADD CONSTRAINT PK_dropoff_location_dim PRIMARY KEY (dropoff_location_id);

ALTER TABLE dbo.payment_type_dim
ADD CONSTRAINT PK_payment_type_dim PRIMARY KEY (payment_type_id);

ALTER TABLE dbo.trip_distance_dim
ADD CONSTRAINT PK_trip_distance_dim PRIMARY KEY (trip_distance_id);

ALTER TABLE dbo.fact_table
ADD CONSTRAINT PK_fact_table PRIMARY KEY (trip_id);

ALTER TABLE dbo.fact_table
ADD CONSTRAINT FK_fact_datetime FOREIGN KEY (datetime_id) REFERENCES dbo.datetime_dim(datetime_id);

ALTER TABLE dbo.fact_table
ADD CONSTRAINT FK_fact_passenger_count FOREIGN KEY (passenger_count_id) REFERENCES dbo.passenger_count_dim(passenger_count_id);

ALTER TABLE dbo.fact_table
ADD CONSTRAINT FK_fact_trip_distance FOREIGN KEY (trip_distance_id) REFERENCES dbo.trip_distance_dim(trip_distance_id);

ALTER TABLE dbo.fact_table
ADD CONSTRAINT FK_fact_rate_code FOREIGN KEY (rate_code_id) REFERENCES dbo.rate_code_dim(rate_code_id);

ALTER TABLE dbo.fact_table
ADD CONSTRAINT FK_fact_pickup_location FOREIGN KEY (pickup_location_id) REFERENCES dbo.pickup_location_dim(pickup_location_id);

ALTER TABLE dbo.fact_table
ADD CONSTRAINT FK_fact_dropoff_location FOREIGN KEY (dropoff_location_id) REFERENCES dbo.dropoff_location_dim(dropoff_location_id);

ALTER TABLE dbo.fact_table
ADD CONSTRAINT FK_fact_payment_type FOREIGN KEY (payment_type_id) REFERENCES dbo.payment_type_dim(payment_type_id);
"""

with engine.connect() as conn:
    conn.execute(text(add_constraints_sql))
    print("Constraints added successfully")
