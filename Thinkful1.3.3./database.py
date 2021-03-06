# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:13:39 2016

@author: Erin
"""

import sqlite3 as lite
import pandas as pd

cities = (('New York City', 'NY'), ('Boston', 'MA'), 
          ('Chicago', 'IL'), ('Miami', 'FL'), 
          ('Dallas', 'TX'), ('Seattle', 'WA'), 
          ('Portland', 'OR'), ('San Francisco', 'CA'), 
          ('Los Angeles', 'CA'))
weather = (('New York City',2013,'July','January',62), 
           ('Boston', 2013, 'July', 'January',59), 
            ('Miami', 2013, 'August', 'January', 84),
            ('Chicago', 2013, 'July', 'January',59),
            ('Dallas', 2013, 'July', 'January', 77),
            ('Seattle', 2013, 'July', 'January', 61),
            ('Portland', 2013, 'July', 'December', 63),
            ('San Francisco', 2013, 'September', 'December', 64),
            ('Los Angeles', 2013, 'September', 'December', 75))
            
con = lite.connect('getting_started.db')

# Select all rows and print the result set one row at a time
with con:

  cur = con.cursor()
  cur.execute ("DROP TABLE IF EXISTS cities")
  cur.execute ("DROP TABLE IF EXISTS weather")
  cur.execute ("CREATE TABLE cities (name text, state text)")
  cur.execute ("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
  
with con:
    
  cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
  cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
  
with con:
  
  cur = con.cursor()
  cur.execute ("SELECT name, state FROM cities INNER JOIN weather ON name=city WHERE warm_month = 'July'")
  

  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows, columns=cols)
  
  
  print ("The cities that are warmest in July are:")
  print (df)
  
  
  
  
  
  
  
  
  
  