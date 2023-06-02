#Databases are everywhere, from a file on your iPhone that stores contacts to massive servers at Facebook containing every 
#detail they can get about you. Think of them like servers with lots of spreadsheets.
#Many people and applications access them at a time, make changes, and relate data in the tables to each other for efficiency.
#Here you'll take some API data and store it in a local database table, similar to a CSV.

#Install the VSCode extension SQLite Viewer, run the code, and click on the new databasing.db file in your VSCode directory.
#Try to understand each step of the process, and if you want try to modify it with your own SQL queries.

import json
import requests
import sqlite3 #A basic database engine that stores the database in a file on your computer

startFreq = input("Enter start of frequency range in MHz, minimum 225: ")
endFreq = input("Enter end of frequency range in MHz, maximum 3700: ")
tableName = "Spectrum"

con = sqlite3.connect("databasing.db") #Automatically create and connect to the database 
cur = con.cursor() #Create a cursor(an object that selects data in and operates on the table)

#Create the table if it doesn't exist
cur.execute(f"CREATE TABLE IF NOT EXISTS {tableName} (id, lowerBand, upperBand, bandDesc)")

#Clears all data from table, columns will not be deleted. The cur.execute statements are SQL(Structured Query Langauge) commands.
#SQL is the main language used to communicate with databases. Most data breaches occur because of a SQL-based vulnerability like SQL injection/SQLi.
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
