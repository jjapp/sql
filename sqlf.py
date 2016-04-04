# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 10:57:35 2016

@author: appertjt
"""

#SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c=connection.cursor()
    
    #use a for loop to iterate through the database, printing the results line by line
    for row in c.execute("SELECT firstname, lastname from employees"):
        print row
        