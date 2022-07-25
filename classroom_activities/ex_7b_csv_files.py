""" "ex_7b_csv_files.py" --- Writing & Reading Spreadsheet Files, specifically CSV files.
In this lesson will we will use the Python programming language to work with "comma-separated-value" or "CSV" files, 
   which are only one of several types of spreadsheet files.
Background: CSV files may include multiple data records with each data record located on its own line.  Each data 
   record (i.e., each line in the file) may include multiple pieces of data separated by commas.  On each line, the pieces of data are always stored in the same sequence.  When saved, the filee name should end with the file extension ".csv"

[UPDATE THIS. ]In this lesson, we will start by making Python create or write a CSV file.  Alternatively, a CSV file may be manually
  created using a text editor or MS Visual Studio Code, as examples.  Subsequently, we will create a simple Python program to read data from the CSV file.
"""

#1: Manually create a CSV file
# Using a text editor or MS Visual Studio Code, type or copy the data shown below and 
#    save it with the file name:  "ex_7b_data1.csv":
# NOTE: Remove the pound sign (#) and any leading space from each line of data.  
# The first is a header line, which describes the prescribed data sequence.  Include it.
#
# name_last,name_first,department,years_employed
# Grantham,Bob,shipping,5
# Oligarch,Chris,management,13
# Smith,Sarah,customer service,12
# LeBlu,Samatha,shipping,7
# Salad,Leslie,customer service,8
# Lasiter,ben,customer service,10
# Wolfslayer,Kyle,shipping,3

#2 - Goal:  Write data to a CSV file.  This will create a new file or will over-write an existing file.
# Try this:
