# Uber_Data_Engineering
# End-to-End Taxi Data Analytics Project

## Overview

This project demonstrates an end-to-end data analytics pipeline:
- Data model design using a star schema
- ETL pipeline in Python to transform and load data into SQL Server with all constraints
- Data visualization using Power BI connecting to the SQL Server database

## Data Model

The star schema includes fact and dimension tables capturing ride details, passenger count, trip distance, locations, rate codes, and payment types.



## ETL Pipeline

- Implemented in Python using Pandas and pyodbc/sqlalchemy for loading data into SQL Server.
- Includes data cleaning, transformation, and enforcing foreign key constraints.
- Python script: `etl/ETL_uber.py`

## SQL Server Database

- connect to your db via `sql/db_connect.py`.
-  queries and scripts in `sql/tosql.py`.

## Power BI Dashboard

- Interactive dashboards created in Power BI Desktop.
- Key visuals include total rides, revenue, passenger counts, payment methods, and location analysis.
- Power BI file: `powerbi/dashboard.pbix`
- Exported report: `powerbi/dashboard_export.pdf`




