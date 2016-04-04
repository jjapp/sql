# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 10:59:47 2016

@author: appertjt
"""

#SELECt statement, remove unicode characters

import sqlite3

with sqlite3.connect("new.db") as connection:
    c=connection.cursor()
    
    c.execute("SELECT firstname, lastname from employees")
    
    #fetchall() retrieves all from the query
    
    rows=c.fetchall()
    
    #output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1]
        
        
