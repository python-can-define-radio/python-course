## 1
## Try this.
print("If you want to put everything", end="")
print("on one line, then you can", end="")
print("use this.")


## 2
## Try this.
mypersondata = {
  "firstname": "Bob",
  "lastname": "Smith",
  "age": 23
}
print(mypersondata["firstname"])


## 3
## Copy and modify the previous example so that it displays the last name instead of the first name.


## 4
## Try this.
mypersondata = {
  "firstname": "Bob",
  "lastname": "Smith",
  "age": 23
}
print(f'Do you know {mypersondata["firstname"]} ...?')
# NOTE: on previous line, we must use diferent types of quotation marks for the f-string vs. the dictionary address.


## 5
## Copy and modify the previous example so that it displays this:
##   "Did you know that ___   ___ is ___ years old?"
##   (Fill in the first name, last name, and age appropriately.)
