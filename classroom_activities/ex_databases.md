# Creating a Database using Python   

Databases are everywhere, from a file on your iPhone that stores contacts to massive servers at Facebook containing every detail they can get about you. Think of them like servers with lots of spreadsheets.   
Many people and applications access them at a time, make changes, and relate data in the tables to each other for efficiency.   
Here you'll take some API data and store it in a local database table, similar to a CSV.  
  
SQL is the main language used to communicate with databases. Most data breaches occur because of a SQL-based vulnerability like SQL injection/SQLi.

### INSTRUCTIONS:
 - a) If using MS VSCode, install the VSCode extension SQLite Viewer, 
 - b) type and run the python program (below), and   
 - c) click on the new databasing.db file in your VSCode file "explorer", and tell VSCode to open it.  
 
Try to understand each step of the process, and if you want try to modify it with your own SQL queries.

### The program:
```python3
""" Database creation using data extracted from FCC website 

Purpose: To create a dabase and maniplate it using SQL (Structured Query Languange) commands
"""

import json     #JSON (JavaScript Object Notation) ref:https://docs.python.org/3/library/json.html
import requests
import sqlite3  # A basic database engine that stores the database in a file on your computer

startFreq = input("Enter start of frequency range in MHz, minimum 225: ")
endFreq = input("Enter end of frequency range in MHz, maximum 3700: ")
tableName = "Spectrum"

con = sqlite3.connect("databasing.db") #Automatically create and connect to the database 
cur = con.cursor()  # In the database, create a cursor, which is an object that selects data in and 
                    # operates on the database or a table (created below).

#Create the table if it doesn't exist
cur.execute(f"CREATE TABLE IF NOT EXISTS {tableName} (id, lowerBand, upperBand, bandDesc)")

#Clear all data from table, columns will not be deleted. The cur.execute statements are SQL(Structured Query Langauge) commands.
cur.execute("SELECT * FROM Spectrum")
cur.execute("DELETE FROM Spectrum")

#Acquire and transform the data, prepare variables for use in the for loop
response = requests.get(f"http://data.fcc.gov/api/spectrum-view/services/advancedSearch/getSpectrumBands?frequencyFrom={startFreq}&frequencyTo={endFreq}&pageNum=1&sortColumn=lowerBand&sortOrder=asc&pageSize=1000&limit=100&format=json")
content = response.text
contentDict = json.loads(content)
spectrumList = contentDict["SpectrumBands"]["SpectrumBand"]

#For each frequency range, insert the values into the table
for band in spectrumList:
    specID = band["id"]
    specLow = band["lowerBand"]
    specHigh = band["upperBand"]
    specDesc = band["bandDesc"]
    cur.execute(f"""
        INSERT INTO {tableName} (id, lowerBand, upperBand, bandDesc)
        VALUES ({specID}, {specLow}, {specHigh}, "{specDesc}");
        """)
con.commit()
con.close()
'''
