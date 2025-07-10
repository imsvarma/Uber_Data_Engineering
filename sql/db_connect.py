# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 16:59:01 2025

@author: imani
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 23:57:28 2025

@author: imani
"""
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, DateTime, DECIMAL, ForeignKey
from sqlalchemy import create_engine

server = 'MANIKANTAVARMA'
database= 'uberetl'
driver = 'ODBC Driver 17 for SQL Server'
connection_string = f"mssql+pyodbc://@{server}/{database}?driver={driver.replace(' ', '+')}&trusted_connection=yes"
engine = create_engine(connection_string)

metadata = MetaData()

