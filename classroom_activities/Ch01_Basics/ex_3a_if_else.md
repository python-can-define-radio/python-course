# If-Else Statements

ℹ️ This material coincides with material from python slideshow C (slides 39-46). 

### Introduction
So far we have been instructing a computer through Python programming to execute a series of commands without any decisions being made as the program runs.  But, computers and the Python language can do so much more.

In a basic definition, a computer is a machine that can make decisions.  In contrast, a pure calculator evaluates mathematical functions but cannot make decisions <sup>[ footnote 1](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch01_Basics/ex_3a_if_else.md#references--footnotes)</sup>.  So, if a computer is useful for making decisions, how do we progam it to do so?  ...I'm glad you asked.

First, let's consider: How do we make a decision?  Wait, take one step back.  WHY do we make decisions?  As we live, work, or play, we make decisions when confronted with multiple options of what to do next.  For example, while riding a bicycle you may come to a fork in the road.  You cannot travel both directions simutaneously.  Which way will you (should you) choose? --Now we are discussing "HOW to make a decision".--  Maybe you have mental instructions based on past experience,  maybe a friend has advised you to go left or right, maybe you have a map, or maybe you notice one path is well worn from frequent use while the other path appears much less traveled. So, you consider the options based on your knowledge, your preference, or pre-established rules.  You then make a decision and direct the bicycle down the chosen path.  

To reminisce for just a moment, I recall coming to a fork in the road several years back.  Initially unsure which way to go, I ultimately chose the path less-traveled, and it has made all the difference <sup>[ footnote 2](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch01_Basics/ex_3a_if_else.md#references--footnotes)</sup>.

Back to computers.  One way to make decisions in a programming language such as Python is by using if-statements. We can use if-statements to compare a recently obtained value against a known value or range of values.  Based on the result of this comparison, the if-statement chooses whether to perform another operation or to skip it.  

The exercises below will allow you to understand how to use if-statements, and ideally, how to appreciate them.

### Exercises using If/Else

When an else-statement follows an if-statement, the computer chooses between performing the `if` (first) operation or the `else` (second) operation.

```python3
## 1
## Try this. Notice that it will ask for input. 
thename = input("What is your name? ")
if thename == "george":
    print("Are you named after the first US President?")
else:
    print("Hello.")


## 2
## Change the previous example so that if the
## user types "bob", it will reply "Are you the painter?"


## 3
## Try this.
name = input("What is your name? ") 
if name == "joe": 
    print("Your name rhymes with low.") 
else: 
    print(f"Hey {name}.") 
    
 
## 4
## Modify the above example so that if the name is
## "Pluto", it will say "Is it a planet or not?" 
```

You'll notice that in the "joe" example above , the user must type "joe" lowercase.  
Here's how to make it so any capitalization works ("Joe", "JOE", etc):

```python3
## 5
## Try this.
name = input("What is your name? ")
print(f"The lowercase version of that is {name.lower()}.")
if name.lower() == "joe": 
    print("Your name rhymes with low.") 
else: 
    print(f"Hey {name}.")


## 6
## Copy and modify the previous example so that
## if the name is "Ruby", it displays
## "That name is also the name of a gem."
## Make it work for any capitalization of Ruby.
########################
##  INSTRUCTOR-CHECK  ##
########################
```

What do you think the != operator means in the following example?

```python3
## 7
## Try this. 
name = input("What is your name? ")
if name.lower() != "jay": 
    print("Your name is not Jay.") 
print("Greetings.")


## 8
## - Ask the user for a name
## - If the name is anything other than Bob, then
##   display "I don't think I know you. I only know Bob."
## Hint: the != operator is a comparison operator meaning "not equal".


## 9
## - Ask the user for a number
## - If the number is not equal to 5, say "You should have picked 5." 
## (Use the != operator)
    

## 10
## - Ask the user for a name
## - If the name is empty, say "You didn't type anything!"
## - Otherwise, say "Hi ___."
## Hint: an empty name would be quotes with nothing inside, so
##     you might use something similar to this piece of code:
##     if whatTheUserTyped == "":
##           print("Something would go here.")
```

```python3
## 11
## Try this. 
age = 10 
ageNextYear = age + 1 
print(ageNextYear) 
     

## 12
## Try this. Note: you will get an error. 
age = input("How old are you?") 
ageNextYear = age + 1 
print(ageNextYear) 
     

## 13
## Try this. 
age = int(input("How old are you?")) 
ageNextYear = age + 1 
print(ageNextYear) 


## 14
## Write a program that satisfies the following examples.
## Remember that the "✎" indicates user input.
## Example 1:
##   How old are you? ✎ 55
##   I see you are 55 years old.
##   You will be 65 years old in 10 years.
## Example 2:
##   How old are you? ✎ 45
##   I see you are 45 years old.
##   You will be 65 years old in 20 years.
########################
##  INSTRUCTOR-CHECK  ##
########################
```

```python3
## 15
## Try this. Note: you will get an error. 
age = input("How old are you?") 
if age < 21: 
    print("You can't drink alcohol in the US yet.") 
else: 
    print("You are legally allowed to drink. Drink responsibly 😊 ") 
     

## 16
## Copy and modify the above example so it works.
## You’ll use the `int` function. 

 
## 17
## Copy and modify the above example so that
## it shows how many years remain until you can
## drink (but only display that if you’re
## under the drinking age). 


## 18
## Write a program that takes a name from the user.
## If the name is the letter "A", say
## "Your name is just the letter A? That’s kinda cool".
## Otherwise, say "Ok, your name is ___". 
```  

### Using elif

One or more elif-statements can be positioned between an if-statement and an else-statement to choose between more than two options or operations.

```python3
## 19
## Try this: 
birthyear = int(input("Type a year: ")) 
if birthyear < 2000: 
    print("You were born before 2000.") 
elif birthyear == 2000: 
    print("You were born in 2000.") 
else: 
    print("You were born after 2000.") 

    
## 20
## Try this:
name = input("What is your name? (type it lowercase please.)")
print("Ok, let me look up that name...")
if name == "bob":
    print("That name used to be common, I think.")
elif name == "sue":
    print("Your name also refers to a legal action.")
elif name == "rob":
    print("Another abbreviation for robert, correct?")
elif name == "lacy":
    print("Does the origin of your name relate to lace?")
else:
    print("I don't know you.")
print("Done.")
```

How is this next example different from the previous example?  
Note: The difference is subtle, so ask if you are unsure.

```python3
## 21
## Try this. 
name = input("What is your name? (type it lowercase please.)")
print("Ok, let me look up that name...")
if name == "bob":
    print("That name used to be common, I think.")
if name == "sue":
    print("Your name also refers to a legal action.")
if name == "rob":
    print("Another abbreviation for robert, correct?")
if name == "lacy":
    print("Does the origin of your name relate to lace?")
else:
    print("I don't know you.")
print("Done.")


## 22
## Here's an example of using separate if statements,
## that is, a case where you would NOT want to use elif:
name = input("What is your name? (type it lowercase please.)")
print("Ok, let me look up that name...")
if name.startswith("z"):
    print("Your name starts with a Z. That is somewhat uncommon in English.")
if len(name) < 3:
    print("Your name is less than 3 characters long.")
if len(name) > 9:
    print("Your name is more than 9 characters long.")
if name == "":
    print("Your name is empty!")


## 23
## Here's another example of the usefulness of elif.
heightInInches = int(input("Give me a number: "))
if heightInInches < 0:
    print("You can't have a negative height!")
elif heightInInches <= 55:
    print("That's relatively short.")
elif heightInInches <= 72:
    print("That's around average.")
else:
    print("That's pretty tall.")


## 24
## Copy and modify the previous example so that each `elif` is
## simply `if`. How does it act differently? 
```

```python3
## 25
## Ask the user how many French fries they want.
## Display different responses depending on how many they
## request. (Examples: "That’s way too many!", etc.) 

 
## 26
## Try this. Did it print what you expected?
x = int(input("Enter a number: ")) 
if x < 20: 
    print("A") 
    print("B") 
print("C") 


## 27
## Copy and modify the previous example so
## that C is only printed if the number is not less than 20.
## Use the `else` keyword.


## 28
## Copy and modify the previous example so that it acts like this:
## if x is less than 20, then print A.
## Otherwise, print C.
## After all of that is done, print Goodbye
## (regardless of what x was.)
```

```python3
## 29
## Try this.
x = int(input("Type a number: "))
if x > -10 and x < 0:
    print("x is more than -10 and less than 0.")


## 30
## Here's a shorter way to write the same example:
## Note: This cannot be done in BlockPy because
##  it incorrectly adds parentheses in the `if`;
##  simply use the long form shown in the previous exercise.
x = int(input("Type a number: "))
if -10 < x < 0:
    print("x is more than -10 and less than 0.")
    

## 31
## Ask the user for a number.
## If the user gives a number more than 50, 
##    then ask "What is your name?"
##    and display "Hello" followed by the name.
## If the user gives any other number,
##    then ask "How did you pick that number?"
##    and regardless of what they say, display "I see."
## After all of that, say "Have a good day."


## 32
## Write a program that takes a number from the user.
## Display the number doubled.
## Then do a sequence of creative if statements of your choice.
##   For example, if the number is negative,
##   display "Really? Negative? Interesting".


## 33
## Try this. Why do we use float instead of int here?
firstcost = float(input("How much is the first thing you bought? "))
secondcost = float(input("How much is the second thing you bought? "))
total = firstcost + secondcost
discounted = total * 0.9
print(f"""The total cost would be {total}.
However, we're doing a special sale today, so you get a 10% discount.
That means you actually pay {discounted}""")
```

```python3
## 34
## Ask the user for the cost of a single item.
## Ask the user for the quantity purchased.
## Print the total cost. 
## Make sure this works for non-integer costs.
## For example, try a cost of 2.30 and quantity of 2.
## Hint: You'll use float instead of int.
## Example:
##   What is the cost for an item? ✎ 2.30
##   How many did you buy? ✎ 2
##   The total cost would be $4.60.


## 35
## Modify the previous example so that the shop gives
## a discount of 10% if you buy at least 20 of an item.  
## For example, if one item costs $5, and you’re buying 20,
## the total cost would be $90. 
     

## 36
## Ask the user for a number.
## Make sure to allow for non-whole numbers.
## Print the absolute value of the
## number without using the abs function. 


## 37
## Ask the user for a temperature in Celsius,
## and display the temperature in Fahrenheit. 
## Make sure to allow for non-whole numbers.


## 38
## Same as previous example, but backwards. 


## 39
## Combine the two previous examples: ask the user for
## a number and which way to convert. 
########################
##  INSTRUCTOR-CHECK  ##
########################


## 40
## Ask the user for a number.
## Using the % operator, display "The remainder of
## your number divided by 5 is ___."
## Also, if the remainder that you calculated is 0,
## display "That number is evenly divisible by 5."

```

What if there's more than one choice that leads to the same outcome? Here are four ways to handle that.

```python3
## 41
## Try this.
color = input("What color is water? ")
if color == "blue" or color == "transparent":
    print("Yes, I agree.")
else:
    print("I'm not sure about that.")


## 42
## Try this.
color = input("What color is water? ")
if color in ["blue", "transparent"]:
    print("Yes, I agree.")
else:
    print("I'm not sure about that.")


## 43
## Try this.
color = input("What color is water? ")
if color != "blue" and color != "transparent":
    print("I'm not sure about that.")
else:
    print("Yes, I agree.")


## 44
## Try this.
color = input("What color is water? ")
if color not in ["blue", "transparent"]:
    print("I'm not sure about that.")
else:
    print("Yes, I agree.")


## 45
## Ask the user what sound a dog makes.
## If the user says any of "woof", "bark", or "ruff",
## then display "That's correct!"
## otherwise, display "Not quite."
## Make it work for any capitalization.

```

### Optional exercise

<details><summary>Expand here for additional content.</summary>


As you have seen, you can use `float` instead of `int` when dealing with non-whole numbers.

```python3
## 46
## Try this.
x = float(input("Type a non-whole number. "))
print(f"One more would be {x + 1}.")
```

Using floats can cause weird rounding errors. 

```python3
## 47
## For example:
print(1.03 - 0.42)
```

This example will print 0.6100000000000001.  

```python3
## 48
## That's quite important when doing comparisons like this:
if 0.1 + 0.1 + 0.1 == 0.3:
    print("This will not print.")
else:
    print("This will print... what is math??")
```

The reason is because the numbers are converted to binary behind the scenes, and just as you can't express "one third" exactly in decimal (0.33333 is not EXACTLY one third) you also can't express "one tenth" exactly in binary.  
For more info, see https://docs.python.org/3/tutorial/floatingpoint.html  
If you plan to eventually do any "real-life" programming, then it's definitely worth reading.

</details>

### References & Footnotes:  
&nbsp;&nbsp; (1) https://techdifferences.com/difference-between-calculator-and-computer.html  
&nbsp;&nbsp; (2) So said the poet Robert Frost.
