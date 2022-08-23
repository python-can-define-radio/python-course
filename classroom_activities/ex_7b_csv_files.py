""" "ex_7b_csv_files.py" --- Writing & Reading Spreadsheet Files, specifically CSV data files.
In this lesson will we will use the Python programming language to work with "comma-separated-value" or "CSV" files, 
   which are only one of several types of spreadsheet files.
Background: CSV files may include multiple data records with each data record located on its own line.  Each data 
   record (i.e., each line in the file) may include multiple pieces of data separated by commas OR another character used as a "delimiter".  
   On each line, the pieces of data are always stored in the same sequence.  By convention, the file name should end 
   with the extension ".csv"
In this lesson, we will start by manually creating a csv file using a text editor or MS Visual Studio 
   Code, as examples.  Subsequently, we will create a simple Python program to read and evaluate data from the CSV file.
Each task is numbered.  
ref:    csv module: https://docs.python.org/3/library/csv.htm, 
        examples: https://realpython.com/lessons/reading-csvs-pythons-csv-module/
Additional tutorials may be available at: https://realpython.com/python-csv/ . The suitability of all portions this website has not been verified.
"""

#1: Manually create a CSV file.
# Using MS Visual Studio Code or a text editor, type or copy the data shown below and 
#    save it with the file name:  "ex_7b_data1.csv". 
# NOTEs: a. Remove the pound sign (#) and the leading space from each line of data.
# b. The first ;line is a header line, which describes the prescribed data sequence.
#    Because there is a header line, we will use the "csv.DictReader" command to retrieve 
#    the data.  This will generate a dictionary data structure for the data.
# c. Some names in the list are intentionally not capitalized.
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
# simmering,Lance,receiving,5

#2: Create a Python program to read the CSV file & report each record
#   (Note: A record = one row of data in the CSV file.)
# [Try this:]
import csv     # ("csv" is a built-in module of Python. All programs herein will need this.)

with open("ex_7b_data1.csv") as csv_file:
    csv_data = csv.DictReader(csv_file, delimiter=",")
    print()    #Gives a blank line to separate output from what precedes it.
    # Print all rows of the data & then close the file after reaching the end.
    print("The rows in the data set are:")
    for row in csv_data:
        print(row)
    print()

#3: Modify the previous program to read & report all fields from each record/row in sentance format.
#   ref: https://realpython.com/lessons/reading-csvs-pythons-csv-module/, accessed July 25, 2022
#   [Try this:]
with open('ex_7b_data1.csv') as csv_file:
    csv_data = csv.DictReader(csv_file, delimiter=',')
    line_count = 0      #This variable will be used to add line numbering to the output.
    print("\nEmployee Report")
    for row in csv_data:
        line_count += 1
        print(f'{line_count}) {row["name_first"]} {row["name_last"]} works in the {row["department"]} ', end='')
        print(f'department, and has been employed with our company for {row["years_employed"]} years.')

#4  Find employees within the list whose last name starts with “s”, irrespective of the capitalization.
#   Enhancement: Use only one criteria when testing the name.

#5: Select & display only the records for which the employee has worked at company for 10 years or more.

#6: Report a one-time bonus for each employee based on number of years employed by the company.
#   For less than 5 years of service $200, for 5 years but less than 10 years $500, for ten or more years $800
#   Enhancement: define a function to print the result.

#7 --  WRITE data to a CSV file.  This will create a new file or will over-write an existing file.
# Try this:
csv_extrn2 = "ex_7b_data2.csv"  
# Data to write to the file, stored in a list of lists:
employees_more = [["Carver", "George Washington", "new product development", 45],
                  ["Newton", "Isaac", "R&D", 48]]

print(f"\nTask 7: Write employee data to a file named {csv_extrn2}.")
with open(csv_extrn2, 'w', newline='') as csv_file:
    field_names = ['name_last','name_first','department','years_employed']
    writer = csv.DictWriter(csv_file, fieldnames = field_names, delimiter=",")  #Prepares an abreviated file-pointer
    writer.writeheader()
    # Establish a new variable "record" and assign data sets to it in sequence:
    for record in employees_more:
        writer.writerow({'name_last': record[0], 'name_first': record[1], 'department': record[2], 
                        'years_employed': record[3]})
# after exiting the "with" command, the external file writing session will be closed.
print(f"Data writing to file '{csv_extrn2}' is completed.")

# Task 8 --  WRITE more data to a CSV file -- append, do not over-write, an existing file.
# Append data from the 1st data file to the 2nd data file created in Task 7. Where:
#     "ex_7b_data1.csv"  # Source of more data
#     "ex_7b_data2.csv"  # Destination
# SUGGESTION: This can be done using two, nested "with open()" commands.  The first opens the writing file, and 
#             the 2nd may be nested in the first and opens the data file.
