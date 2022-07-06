## Preliminaries:
## - Install pandas using pip. (Don't use conda.) Ask the instructor how, or see pandas.pydata.org
## - Download the fake smoker data csv file from our classroom_activities folder.
##   (Sidenote for those who are interested: the code I used to generate the fake smoker data is at the bottom of this file.)

import pandas as pd

## Setup
fakeSmokerData = pd.read_csv("fake_smoker_data.csv")

## 1
print(fakeSmokerData)

## 2
## This is just the index of those who started smoking before age 20.
print(fakeSmokerData["age_started_smoking"] < 20)

## 3
## If we want to see the rest of the data for those rows, we do this.
print(fakeSmokerData[fakeSmokerData["age_started_smoking"] < 20])

## 4
## We can see how many people strted smoking before 20:
below20 = fakeSmokerData[fakeSmokerData["age_started_smoking"] < 20]
print(len(below20))







###### Appendix
###### For those who are interested:
###### This is the code that I used to generate the fake smoker data.
# import random
# for unused in range(20):
#     st = random.randrange(18, 23)
#     curr = random.randrange(20, 65)
#     g = random.choice("FM")
#     print(f"{st},{curr},{g}")
