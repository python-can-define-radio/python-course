""" "ex_7b_csv_files.py" --- Writing & Reading Spreadsheet Files, specifically CSV files.
In this lesson will we will use the Python programming language to work with "comma-separated-value" or "CSV" files, 
   which are only one of several types of spreadsheet files.
Background: CSV files may include multiple data records with each data record located on its own line.  Each data 
   record (i.e., each line in the file) may include multiple pieces of data separated by commas.  
   On each line, the pieces of data are always stored in the same sequence.  When saved, the file name should end 
   with the file extension ".csv"
In this lesson, we will start by manually creating a csv file using a text editor or MS Visual Studio 
   Code, as examples.  Subsequently, we will create a simple Python program to read and evaluate data from the CSV file.
Each task is numbered.  Additional tutorials are available at: https://realpython.com/python-csv/ .
"""

#1: Manually create a CSV file.
# Using MS Visual Studio Code or a text editor, type or copy the data shown below and 
#    save it with the file name:  "ex_7b_data1.csv":
# NOTE: Remove the pound sign (#) and any leading space from each line of data.  
# The first is a header line, which describes the prescribed data sequence.  Include it.
#
# name_last,name_first,department,years_employed
# Grantham,Bob,shipping,5
# Oligarch,Chris,management,13
# Smith,Sarah,customer service,12
# Lasiter,Samatha,shipping,7
# Zepher,bob,shipping,4
# Salad,Leslie,customer service,8
# LeBlu,ben,customer service,10
# Wolfslayer,Kyle,shipping,3

#2: Read data from a CSV file and report all data from each record/row using a sentence.
#   ref: https://realpython.com/lessons/reading-csvs-pythons-csv-module/, accessed July 25, 2022
#   [Try this:]
import csv
with open('ex_7b_data1.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    print()
    for row in csv_reader:
        line_count += 1
        print(f'{line_count}) {row["name_first"]} {row["name_last"]} works in the {row["department"]} ', end='')
        print(f'department, and has been employed with our company for {row["years_employed"]} years.')

#3: Select the records having a first name of "Bob", irrespective of the capitalization in the data.
#   Enhancement: use only one criteria when testing the name.

#4: Select & display only the records for which the name starts with ???b???. 

#5: Select & display only the records for which the employee has work at company for 10 years or more.

#6: Report a one-time bonus for each employee based on number of years employed by the company.
#   For less than 5 years of service $200, for 5 years but less than 10 years $500, for ten or more years $800
#   Enhancement: define a function to print the result.
