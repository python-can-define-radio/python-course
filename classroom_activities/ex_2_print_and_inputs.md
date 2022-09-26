```python3
#########################
### These exercises take the approach of providing fodder for experimentation.
###
### Here's a good resource for explanations:
###   https://learn.arcade.academy 
###   Start on Chapter 4.
### 
### Some notes about that site:
### - It mentions "Installing the Python programming language". That's already done in our classroom.
### - It mentions "An integrated development environment (IDE) called PyCharm". We primarily use VSCode as our IDE.
### - It mentions the "Version control system" git. Git is not required for this class, but interested readers are encouraged to explore it.
### - Sections 4.2 and 4.3 show how to work in PyCharm. We will "translate" these steps to VSCode together as a class.
#########################

## Setup:
## - Create a file called ex_2.py
## - Type the first exercise in that file
## - Press run
## - Comment (disable) that exercise
## - Try the next exercise
##
## Ask if you have any questions.

## 1 
## Try this.
print("Here we go!")


## 2
## Try this.
## You'll get an error having to do with the quotation marks.
## Why do you think that is? How do you fix it?
print(“bob”)


## 2b
## Try this.
print("If you want \n separate lines, you \n can do it \n like this.")

## 3
## Try this.
firstn = "Bob"
lastn = "Smith"
print(firstn)
print(lastn)


## 4
## Try this.
firstn = "Bob"
lastn = "Smith"
print(f"My name is {firstn} {lastn}")


## 4b
## Try this. When you run it, it will ask you to type something.
print("Hello!")
cartype = input("Say the name of a car, then press enter: ")
print(f"The car you named is {cartype}. That was a good choice.")


## 4c
## Copy and modify the previous example so that it asks the user for the name of a car,
## and then prints "The car you named is ____. Do you have one?"
## In the blank, you should say the car that the user named.


## 4d
## Copy and modify the previous example so that it asks the user for the name of an animal,
## and then prints "The animal you named is ____. I think that it would make a nice pet."


## 5
## Try this.
firstn = input("What is your first name?")
lastn = "Smith"
print(f"Your name is {firstn} {lastn}.")


## 6
## Copy and modify the previous example to do the following:
##  - Ask the user for his/her first name.
##  - Ask the user for his/her last name.
##  - Print "Your name is ___  ___."

## 6b
## Ask the user for their first name, middle name, and last name.
## Print "Your name is __ __ __" (filling in their first name, middle name, and last name).


## 7
## Ask the user for a color, and then say
## "___ is a pretty color."
## (Fill in the blank with the actual color.)


## 8
## Ask the user for the name of an animal and a plant.
## Then display "The ___ eats ___ every day",
## but fill in the blanks with the animal and the plant.


## 9
## Try this.
a = "Hello"
b = "Goodbye"
c = a + b
print(c)


## 10
## Try this.
a = input("First word? ")
b = input("Second word? ")
c = a + b
print(c)


## 11
## Try this.
a = 5
b = 3
c = a + b
print(c)


## 12
## Try this.
a = "5"
b = "3"
c = a + b
print(c)


## 13 
## Try this.
a = int("5")
b = int("3")
c = a + b
print(c)


## 14
## Try this.
a = input("Type an integer.")
b = input("Type another integer.")
c = a + b
print(c)


## 15
## Try this.
a = int(input("Type an integer."))
b = int(input("Type another integer."))
c = a + b
print(c)


## 16
## Try this. You will get an error. How do you fix it?
a = input("Type an integer.")
b = int(input("Type another integer."))
c = a + b
print(c)

## 17
## Try this. You will get an error. How do you fix it?
favnum = input("What is your favorite number?")
onemore = favnum + 1
print(f"One more would be {onemore}.")


## 18
## Ask the user for two integers.
## Display "The sum of your two numbers is ___".


## 19
## Ask the user for two integers.
## Display "The first number minus the second number is ___".


## 20
## Ask the user for an integer.
## Display "That number plus 2 is ___".


## 21
## Ask the user for a number.
## Display "Half of that number is ___".


## 22
## Ask the user for the number of questions on a test,
## and ask "how many did you get right?"
## Then, display "You got ___% right". (You'll need to calculate the percent.)


## 23
##### You may wonder why you must use the int() function.
##### After all, shouldn't the computer know what a number looks like?
##### Here's an example of when you WOULDN'T want the number to be treated as an integer.

########################################
# Right way:
beg = "800"
mid = "555"
end = input("Can you give me some random last four digits please? ")

fullPhoneNum = beg + mid + end
print(fullPhoneNum)


########################################
# Wrong way:
beg = 800
mid = 555
end = int(input("Can you give me some random last four digits please? "))

fullPhoneNum = beg + mid + end
print(fullPhoneNum)

########################################
# Another wrong way:
beg = 800
mid = 555
end = input("Can you give me some random last four digits please? ")

fullPhoneNum = beg + mid + end
print(fullPhoneNum)
```
