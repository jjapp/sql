# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 14:06:13 2016

@author: appertjt
"""

#INSERT Command

#Import the sqlite3 library
import sqlite3

#create the connection object
with sqlite3.connect("new.db") as connection:
    c=connection.cursor()
    c.execute("INSERT INTO population VALUES('New York City', \'NY', 8200000)")
    c.execute("INSERT INTO population VALUES('San Francisco', \'CA', 800000)")




#close the database connection
connection.close()

