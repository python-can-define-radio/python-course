## Preliminaries:
## - Install pandas using pip:
##   In the terminal, type
##     pip install pandas
##
## - Download the fake smoker data csv file from our classroom_activities folder.
##   (Sidenote for those who are interested: the code I used to generate the fake smoker data is at the bottom of this file.)


## 1
## Verifying that the data is available:
f = open("fake_smoker_data.csv")
print(f.readlines())
f.close()


## 2
## Setup
import pandas as pd
fakeSmokerData = pd.read_csv("fake_smoker_data.csv")


## 3
## Try this:
print(fakeSmokerData)


## 4
## This is just the index of those who started smoking before age 20.
print(fakeSmokerData["age_started_smoking"] < 20)


## 5
## If we want to see the rest of the data for those rows, we do this.
print(fakeSmokerData[fakeSmokerData["age_started_smoking"] < 20])


## 6
## We can see how many people started smoking before 20:
below20 = fakeSmokerData[fakeSmokerData["age_started_smoking"] < 20]
print(len(below20))


## 7
## Print the rows of people who are currently older than 50.


## 8
## Try this:
print(fakeSmokerData.sort_values("current_age"))


## 9
## Try this:
print(fakeSmokerData.sort_values("age_started_smoking"))



###### Appendix
###### For those who are interested:
###### This is the code that I used to generate the fake smoker data.
# import random
# for unused in range(20):
#     st = random.randrange(18, 23)
#     curr = random.randrange(20, 65)
#     g = random.choice("FM")
#     print(f"{st},{curr},{g}")
