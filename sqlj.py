# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 16:17:13 2016

@author: appertjt
"""

#Create a table and populate it with data

import sqlite3

with sqlite3.connect("new.db") as connection:
    c=connection.cursor()
    #Drop regions table if exists
    
    c.executescript('drop table if exists regions;')
    
    #resume tutorial
    c.execute("""CREATE TABLE regions (city TEXT, region TEXT)""")
    
    cities = [
                ('New York City', 'Northeast'),
                ('San Francisco', 'West'),
                ('Chicago', 'Midwest'),
                ('Houston', 'South'),
                ('Phoenix', 'West'),
                ('Boston', 'Northeast'),
                ('Los Angeles', 'West'),
                ('Houston', 'South'),
                ('Philadelphia', 'Northeast'),
                ('San Antonio', 'South'),
                ('San Diego', 'West'),
                ('Dallas', 'South'),
                ('San Jose', 'West'),
                ('Jacksonville', 'South'),
                ('Indianapolis', 'Midwest'),
                ('Austin', 'South'),
                ('Detroit', 'Midwest')]
                
    c.executemany("INSERT INTO regions VALUES(?, ?)", cities)
    c.execute("SELECT*FROM regions ORDER BY region ASC")
    
    rows=c.fetchall()
    
    for r in rows:
        print r[0], r[1]
        
        