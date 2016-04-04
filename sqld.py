# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 20:38:46 2016

@author: appertjt
"""

#import from CSV

#import the csv library

import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c=connection.cursor()
    
    #open the csv file and assign it to a variable
    employees=csv.reader(open("employees.csv","rU"))
    
    #delete table if it exists
    c.executescript("drop table if exists employees;")
    #create a new table called employees
    c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
    
    #insert data into table
    c.executemany("INSERT INTO employees(firstname, lastname) values(?,?)", employees)
    
    