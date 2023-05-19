## Do ex_pandas.py exercise before attempting this one

## - Download the sales_data_2022.csv file from our classroom_activities folder.

## 1

import pandas as pd
sales2022 = pd.read_csv("sales_data_2022.csv")
print(sales2022)

## 2
## Print only the brands with over 1 million units in sales

print(sales2022[sales2022["grand_total"] > 1000000])

## 3a
## This is how you sort values by a specific column
## This exercise shows how to sort by descending order

print(sales2022.sort_values("grand_total", ascending=False))

## 3b
## Try sorting by ascending order

## 5a
## Try the following

print(sales2022.nlargest(10, "grand_total"))

# 5b
# Try to narrow the list down to the bottom 10 in sales

# 6a
# This is how you can narrow down to a specific brand on the "brand" column

print(sales2022[sales2022["brand"]=="Subaru"])

# 6b
# You can also select specific columns if you don't want to see all of the data
# You can add and remove as many columns as needed

print(sales2022[sales2022["brand"] == "Subaru"][["grand_total", "brand"]])

# 7a
# This is how you can filter on a brand that starts with a specific letter

print(sales2022[sales2022["brand"].str.startswith("L", na=False)])

# If you want to use .lower() this is how you would do it

print(sales2022[sales2022["brand"].str.lower().str.startswith("l", na=False)])

# 7b
# Try to filter on brands that end with the letter "i"
# Remember Python is case-sensitive


