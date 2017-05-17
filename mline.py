#!/usr/bin/python
'''
Line visualization
'''
import sqlite3

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

# Determine the top 5 locations
cur.execute('''SELECT location, year, total FROM birth''')


data = cur.fetchall()

loc_year = {}
locations = []
years = []
for d in data: 
    if d[1] not in years: 
        years.append(d[1])
    key = (d[0], d[1])
    if key not in loc_year:
        loc_year[key] = d[2]
    if d[0] not in locations:
        locations.append(d[0])

fhand = open('gline.js', 'w')
fhand.write("gline = [ ['Years'")
for location in locations:
    fhand.write(",'"+location+"'")
fhand.write("]")

for year in years:
    fhand.write(",\n['"+str(year)+"'")
    for population in locations:
        key = (population, year)
        val = loc_year.get(key,0)
        fhand.write(","+str(val))
    fhand.write("]")

fhand.write("\n];\n")

print "Data written to gline.js"
