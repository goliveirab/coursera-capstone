#!/usr/bin/pyton
'''
Clean and save data from xml
'''

import pyexcel
import sqlite3

# DataBase: connect and create
conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS birth (
                   id INTEGER UNIQUE,
                   year INTEGER,
                   location TEXT,
                   total REAL,
                   male REAL,
                   female REAL)''')

# Excel doc
records = pyexcel.iget_records(file_name="estadistica02.xls")

for index, record in enumerate(records):
    print( "Index: %s" % (index), "Year: %d" % ( record['Year'] ), " Location: %s" % ( record['Location'] ) )

    cur.execute('''INSERT OR IGNORE INTO birth (
                       id, 
                       year, 
                       location, 
                       total, 
                       male, 
                       female ) 
                   VALUES (?, ?, ?, ?, ?, ?)''',
                  (index, 
                   record['Year'],  
                   record['Location'],
                   record['Total'],
                   record['Male'],
                   record['Female'] ))

conn.commit()
cur.close()
