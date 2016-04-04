# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 14:14:32 2016

@author: appertjt
"""

#executemany() method

import sqlite3

with sqlite3.connect("new.db") as connection:
    c=connection.cursor()
    
    #insert multiple records using a tuple
    cities=[('Boston', 'MA', 6000000),('Chicago', 'IL', 2700000), ('Houston', 'TX', 2100000)]
    
    #insert data into table
    c.executemany('INSERT INTO population VALUES(?,?,?)', cities)