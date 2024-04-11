# For loops

One of the most powerful uses of programming is the ability to repeat an action, such as automatically sending text messages to many recipients. One way to accomplish this is the `for` loop. 

ℹ️ Use Ctrl + C to exit a program (useful for exiting infinite loops).

ℹ️ This material coincides with material from python slideshow C (slides 22-29).

As you work these exercises, Ask yourself the questions, "What lines of code are inside the for-loop, and where does the for-loop end?"

### Exercises

```python3
# 1
# Try this:
colors = ["red", "orange", "yellow"]
for color in colors:
    print("Here is a color that I know:")
    print(color)
    print()
print("\nThe for-loop has ended.")
```
Can you answer the questions, "What items are inside the for-loop, and where does the for-loop end?"?  If not, try again after a few more examples.

The line `for color in colors:` is the new part. It means "for each color in my list of colors, do the following actions."

You can think of it like this:

```python3
# 2
# This is a way to imagine how the code above works.
colors = ["red", "orange", "yellow"]

color = colors[0]
print("Here is a color that I know:")
print(color)
print()

color = colors[1]
print("Here is a color that I know:")
print(color)
print()

color = colors[2]
print("Here is a color that I know:")
print(color)
print()
```

For example, we could greet each name in a list of names:

```python3
# 3
# Try this:
names = ["Sam", "Lisa", "Micah", "Dave"]
for name in names:
    print(f"Hello {name}. Welcome to the Python course.")

    
# 4
# Copy and modify the previous example like so:
# for each name, display "Have a good day, ____. I hope you enjoyed experimenting with python."
# (Fill in the blank with the name.)
```

You can do any operation that you'd like inside of the loop. For example, we could do math on each item in a list:

```python3
# 5
# Try this:
ages = [26, 37, 55, 10, 5]
for age in ages:
    print(f"One of the people in my list is {age} years old.")
    print(f"In two years, that person will be {age + 2} years old.")
    print()


# 6
# Copy and modify the previous example so that for each age,
# it displays "5 years ago, that person was ___ years old."


# 7
# For each of the following numbers, display "Half of __ is ___". For example, "Half of 21 is 10.5"
numbers = [21, 40, 32, 10, 8, 3]
```

You can also use a `for` loop with a range:

```python3
# 8
# Try this:
for num in range(1,5):
    print(num)
```

You'll notice that `range()` always omits the final number. It may seem odd, but it was an intentional decision in the design of Python (and other languages).

Why? The short explanation is that it helps avoid off-by-one errors.

<details><summary>Here are some further explanations (optional reading):</summary>

- https://howdoesinternetwork.com/2015/numbers
- https://howdoesinternetwork.com/wp-content/uploads/E.W.-Dijkstra-Archive-Why-numbering-should-start-at-zero-EWD-831-transcript.html
- https://stackoverflow.com/questions/4504662/why-does-rangestart-end-not-include-end

</details>


```python3
# 9
# Copy and modify the previous example to print the numbers 1 to 6.
```

Here are some examples of using other control structures inside of `for` loops.

```python3
# 10
# Try this.
temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
for temp in temps_in_F:
    print(f"The temperature was {temp}")

    
# 11
# Try this.
temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
for temp in temps_in_F:
    print(f"The temperature was {temp}")
    if temp > 90:
        print("That's hot.")


# 12
# Copy and modify the previous question to display the temperature and display whether it is above or below freezing.
```

As you've now seen, indentation controls whether or not a part of the code inside the for-loop.  If indented, it will be repeated.  Where the indentation ends, the for-loop no longer exists. To practice this concept, try this example below.

```python3
# 12b
# Try this to see the impact of indentation. How do you fix it?
temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40]
for temp in temps_in_F:
    print("Looking at the temperatures.")
print(f"One of the temperatures in the list is {temp}")
if temp > 90:
    print("That's hot.")
```

There may be cases in which you want to count how many items in a list end with a certain string. Before we do that, here's how `endswith` works:

```python3
# 13
# Try this:
x = input("Say a word: ")
if x.endswith("s"):
    print("That ends with an 's', so it might be plural.")
print("That's all I have to say.")


# 14
# Modify the previous example so that if the user input ends with "day",
# then the computer will display "I think that's a day of the week."
```

Let's count. In the example below, we loop through the strings in the `fruits` list, adding one to `berryCount` every time the variable `fr` ends with "berry".

Notice that we must _initialize_ the variable to zero before we start counting. 

```python3
# 15
# Try this:
fruits = ["strawberry", "mango", "raspberry", "blueberry", "grape", "melon"]
berryCount = 0
for fr in fruits:
    if fr.endswith("berry"):
        berryCount += 1
print("I've finished counting the fruits.")
print(f"There were {berryCount} that ended with berry.")


# 16
# Using `startswith` (which works quite similarly to endswith),
# count how many of the fruits start with 'm'.
# Then display the count.
```

Use a count with your for loop to find how many of a certain item meet your criteria.

```python3
# 17
# Given this list, count how many temperatures are above freezing.
# Display the count.
temps_in_F = [90, 30, 47, 82, 68, 100, 25, 40]


# 18
# Copy and modify the previous example to show the user how many
# temperatures are above freezing and how many are below freezing.
```

#### Using lists of objects

Often, you may work with related sets of data. For example, imagine a list of instructors that includes their names, ages, and years of experience. One way to express this data is a list of objects. In the example below, you'll see that we create a dataclass called `Instructor`, and we create a list of five `Instructor` objects. Each object is an "instance" of the class `Instructor`.

```python3
# 19
from dataclasses import dataclass

@dataclass
class Instructor:
    name: str
    age: int
    yearsExp: int

instructors = [
    Instructor("Maria", 38, 7),
    Instructor("Walton", 47, 22),
    Instructor("Martin", 52, 18),
    Instructor("Joel", 28, 3),
    Instructor("Tate", 67, 5)
]
```

You could use this in a `for` loop like so:

```python3
print("Here is my instructor data:")
for person in instructors:
    print(f"The instructor {person.name} is {person.age} years old and has {person.yearsExp} years of experience.")
```

Let's do some math inside of the loop.

```python3
# 20
# Given the instructors list defined above,
# display how old each person was when he/she started this job.
# For example, Maria started this job 7 years ago, so you would print this:
#    The instructor Maria is 38 years old, and started working at age 31.
#
# Note: for this exercise, you cannot add any attributes to the dataclass.
# In other words, this portion must remain unchanged:
@dataclass
class Instructor:
    name: str
    age: int
    yearsExp: int
# Why? The goal is to have Python compute the
# started-working-age within the `for` loop.
# Ask an instructor if this is unclear.  


# 21
# Copy and modify the previous example. In this version, for each instructor,
# display the following:
#     The instructor Maria has been working for 7 years, and will receive a $70 bonus this year.
# 
# The bonus must be $10 times the number of years of experience (5 years would be $50, etc).
# As in the previous exercise, the dataclass must remain unchanged.


# 22
# Copy and modify the previous example.
# Ask the user for the extra bonus per year of experience. Compute appropriately.
# Example run:
#     What is the bonus per year of experience? 20
#     The instructor Maria has been working for 7 years, 
#     and will receive a $140 bonus this year.
#     The instructor Walton has been working for 22 years,
#     and will receive a $440 bonus this year.
#     ...etc...


# 23
# Copy and modify the previous example.
# After the for loop, display
#    "The total amount of work experience for this team is ___". 
# Must compute the total inside the for loop.
# Hint: the structure will resemble this:
#   totalYearsExp = 0
#   for ??? in ???:
#       totalYearsExp += person.yearsExp
#   print(f"The total amount of work experience for this team is {totalYearsExp}")
```

### Optional exercises

_If you have time, we recommend doing the exercises below._

#### Lists of lists:

Another way to store related data is using a list of lists: For example, imagine a list of instructors that includes their names, ages, and years of experience. One way to express this data is a list of lists:

```python3
# 24
instructors = [
    ["Maria", 38, 7],
    ["Walton", 47, 22],
    ["Martin", 52, 18],
    ["Joel", 28, 3],
    ["Tate", 67, 5]
]
```

To work with this list, we may use a `for` loop:

```python3
# 25
# Try this.
instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
                  ["Joel", 28, 3], ["Tate", 67, 5]]
print("Here is my instructor data:")
for instructor in instructors:
    name, age, yearsExp = instructor
    print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")
```

You may be surprised at the line `name, age, yearsExp = instructor`. We're using a special Python feature called **unpacking a list**. We'll unpack that concept (pun intended) in the next few exercises.

```python3
## 26a
## Try this.
## Notice that each variable is assigned to the respective element of the list.
name, color = ["Bob", "Green"]
print(f"{name} likes the color {color}")


## 26b
## This example shows the same concept using an additional variable.
personinfo = ["Bob", "Green"]
name, color = personinfo
print(f"{name} likes the color {color}")


## 26c
## Here's an example that needs to be fixed.
## For the sake of the exercise, only change the labelled line.
personinfo = ["Bob", "Green", 20]
name, age, color = personinfo   #   <-- Only change this line.
print(f"{name} is {age} years old, and likes the color {color}")
```

In the case of a list of lists, you could use a combination of indexing and unpacking, but a `for` loop is often better. Both approaches are shown below.

First, the long (not recommended) way, just for comparison.

```python3
## 27a
## Remember, this is not recommended.
instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
                  ["Joel", 28, 3], ["Tate", 67, 5]]
print("Here is my instructor data:")

instructor = instructors[0]
name, age, yearsExp = instructor
print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

instructor = instructors[1]
name, age, yearsExp = instructor
print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

instructor = instructors[2]
name, age, yearsExp = instructor
print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

instructor = instructors[3]
name, age, yearsExp = instructor
print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")

instructor = instructors[4]
name, age, yearsExp = instructor
print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")
```

Now, the recommended way:

```python3
## 27b
## Try this.
instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
                  ["Joel", 28, 3], ["Tate", 67, 5]]
print("Here is my instructor data:")
for instructor in instructors:
    name, age, yearsExp = instructor
    print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")
```

If you'd like, you can condense this even more:

```python3
## 27c
## This shows the even-more-condensed approach.
instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
                  ["Joel", 28, 3], ["Tate", 67, 5]]
print("Here is my instructor data:")
for name, age, yearsExp in instructors:
    print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")
```

Now that we've learned how unpacking works, let's do some math inside of the loop.

```python3
# 28
# Given this data,
instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
                  ["Joel", 28, 3], ["Tate", 67, 5]]
# Display how old each person was when he/she started this job.
# For example, Maria started this job 7 years ago, so you would print this:
#    The instructor Maria is 38 years old, and started working at age 31.
# 
# Note: For this exercise, the given code must remain unchanged.
# In other words, you cannot do this:
#    instructors = [["Maria", 38, 7, 31]...
#                                    ^^ You cannot add this.
# Why? The goal is to have Python compute the
# started-working-age within the `for` loop.
# Ask an instructor if this is unclear.


# 29
# Copy and modify the previous example. In this version, for each instructor,
# display the following:
#     The instructor Maria has been working for 7 years, and will receive a $70 bonus this year.
# 
# The bonus must be $10 times the number of years of experience (5 years would be $50, etc).
# As in the previous exercise, the list of instructors must remain unchanged.


# 30
# Copy and modify the previous example.
# Ask the user for the extra bonus per year of experience. Compute appropriately.
# Example run:
#     What is the bonus per year of experience? 20
#     The instructor Maria has been working for 7 years, and will receive a $140 bonus this year.
#     The instructor Walton has been working for 22 years, and will receive a $440 bonus this year.
#     ...etc...


# 31
# Copy and modify the previous example.
# After the for loop, display
#    "The total amount of work experience for this team is ___". 
# Must compute the total inside the for loop.
# Hint: the structure will resemble this:
#   totalYearsExp = 0
#   for ??? in ???:
#       totalYearsExp += yearsExp
#   print(f"The total amount of work experience for this team is {totalYearsExp}")
```

Here another example to practice the same concepts:

```python3
# 32
# The following data describes four runners.
# Each sub-list contains, in this order,
#  - the runner's name
#  - the miles that that runner ran
#  - the minutes it took to run that many miles

runners = [
    ["James", 5, 60],
    ["Tom", 1, 7],
    ["Steve", 2, 22],
    ["Carson", 2, 12]
]

# Your task is to print the name and minutes-per-mile for each runner.
# The structure will resemble this:
for ??? in runners:
    print(f"{???} ran {???} miles in {???} minutes.")
    print(f"That means {???} took an average of {???} minutes to run each mile.")
# Note that you may need to add more code than what is shown.
```

#### Other for-loop examples

As you've seen, you can use a `for` loop with lists. You can also use a `for` loop with a string. For example:

```python3
# 33a
# Try this:
phrase = "Hello world"
for letter in phrase:
    print(f"The letter is {letter}")


# 33b
# Copy and modify the previous example so it asks the user for a string (rather than only using "Hello world").


# 34
# Copy and modify the previous example so it outputs each letter from the user input followed by "!". For example:
# H!
# e!
# l!
# l!
# o!


# 35
# For each of the integers 1 to 5, print that number squared.
# Use the range function.
# (In other words, the lists [1, 2, 3, 4, 5] and [1, 4, 9, 16, 25] should not appear in your code.)


# 36
# Copy and modify the previous example to allow the user to specify the highest number rather than stopping at 5.
# Ex:
# Highest number?  (user types 4)
# 1
# 4
# 9
# 16


# 37
# Do you remember the operator that does remainder in Python?
# Use a for-loop to display the following:
#  1 divided by 4 would have a remainder of ____.
#  2 divided by 4 would have a remainder of ____.
# ...
# 10 divided by 4 would have a remainder of ____.
# 11 divided by 4 would have a remainder of ____.
# 12 divided by 4 would have a remainder of ____.
# Here's a hint. You'll most likely change the a, b, and c.
for a in range(b, c):
    print(f"___ divided by 4 would have a remainder of ___")


# 38
# Try this:
print("Hello"*3)


# 39
# Modify the previous example to ask the user how many "Hello"s to print.
# Hint: There are two ways to do this.
#
#   One approach uses a `for` loop, and would resemble this:
#   (Note: you should replace the "???" with actual code)
#
#       howmany = int(input("How many times would you like to print Hello? "))
#       for i in range(???):
#           print("Hello")
#   
#   The second approach is to simply multiply within the print function:
#   howmany = ???
#   print("Hello"*howmany)


# 40
# Construct the following pattern using a `for` loop.
# Let the user specify how many rows to print.
# AAAAA
# AAAAA
# AAAAA
# AAAAA
# 
# Hint:
#     howmany = int(input("How many rows would you like? "))
#     for i in range(???):
#         print("AAAAA")


# 41
# Construct the following using a `for` loop.
# Let the user specify how many rows to print.
# 1 A
# 2 A
# 3 A
# 4 A
#
# Hint:
#     howmany = int(input("How many rows would you like? "))
#     for i in range(???):
#         print(f"{you_the_student_will_fill_this} A")


# 42
# Construct the following using a `for` loop.
# Let the user specify how many rows to print.
# 1 times A is A
# 2 times A is AA
# 3 times A is AAA
# 4 times A is AAAA


# 43
# Construct the following pattern using a `for` loop.
# Let the user specify how many rows to print.
# A
# AA
# AAA
# AAAA


# 44
# Copy and modify the earlier `instructors` example to display each person's name and salary.
# Compute the salary using this formula:
#   For 0 to 4 years, the pay is $35000.
#   For 5 to 9 years, the pay is $36000.
#   For 10 to 14 years, the pay is $37000.
#   etc.
# Hint:
# base_pay = ???
# pay_adjustment = ???
# for name, age, yearsExp in instructors:
#     pay_level = yearsExp // 5
#     salary = base_pay + (pay_adjustment * pay_level)
#     print(f"???")
# Example output: 
#     Maria: 7 years of experience, $36000 per year


# 45
# Copy and modify the previous example.
# Ask the user for...
#  - the base pay, and
#  - the amount of pay adjustment per 5 years of experience.
# Example run:
#     What is the base pay? 55000
#     What is the pay adjustment per 5 years of experience? 2000 
#     Maria: 7 years of experience, $57000 per year


# 46
# Try this. It shows how to use `enumerate`.
names = ["Sam", "Lisa", "Micah", "Dave"]
for indx, elem in enumerate(names):
    print(f"The index is {indx} and the element is {elem}")


# 47
# Now, let's experiment with counting.
# Modify the earlier example (the one that printed "Hello" with "!" after each letter) so it outputs the 
#  indices of the letters before the letters.
# Hint: One way to do this is using enumerate.
# Example output:
# 0: H!
# 1: e!
# 2: l!
# 3: l!
# 4: o!
# Etc.
```

Imagine this context for the next few questions:  
_Your spectrum analyzer is logging which frequencies have shown activity. It makes a note of the center frequency of each burst of activity. Here’s what it has recorded (units are MHz):_

```python3
freqs = [2403.6, 101.3, 90.1, 5.2, 2410.2, 3.7]
```

Given that list of frequencies, complete the following:

```python3
# 48
# Using a loop, print each frequency, and then print whether it is
# in the Wi-Fi range, the FM Radio range, or Neither Wi-Fi nor FM.


# 49
# Modify the previous example to count how many frequencies were in each category.
# At the end of the program, print the count for each category.


# 50
# A report is being produced which only shows detected Wi-Fi frequencies.
# Make a copy of the previous program that only prints the Wi-Fi frequencies from the list.


# 51
# After having read the report, someone wants to know where in the list that the Wi-Fi
# frequencies occur. Make a program that prints both Wi-Fi frequencies and their indices.
# You'll most likely want to use the enumerate function.

# Expected output:
# 2403.6 MHz: index 0
# 2410.2 MHz: index 4


# 52
# Some of the audience of the report is unfamiliar with MHz.
# Modify one (any one) of the above spectrum-related questions
# to allow the user to choose if they want to see the results in MHz or GHz.
# Then print the frequencies using the chosen unit.


# 53
# Someone now wants a program to convert between MHz and GHz.
# The person wants to be able to type everything in one prompt, for example,

#   What would you like to convert? 3445 MHz
#   That is 3.445 GHz.

# Convert appropriately from MHz to GHz or vice versa using input from a single prompt.
# Note 1: the following exercise provides a useful hint.
# Note 2: You can assume the user enters valid data, or, for a challenge, check for data validity.


# 54
# Try this:
userdata = input("Enter two numbers, separated by a space.")
a, b = userdata.split()
print(f"First number: {a} and second number: {b}")
```

### Nested for-loops

These exercises can be done using a for loop inside another for loop.

```python3
# 55: nested for-loops
# (challenge question)
# Display multiplication facts from 1 to 5:
# 1 * 1 = 1
# 1 * 2 = 2
# ...
# 1 * 5 = 5
# ...
# 3 * 4 = 12
# ...
# 5 * 1 = 5
# ...
# 5 * 5 = 25

# 56: nested for-loops -- Multiplication table 
# (challenge question)
# Using the nested for-loops you created to display multiplication facts from 1 to 5 (above),
# display the results in a table:
#
#    | 1   2   3   4   5
#  --|------------------
#  1 | 1   2   3   4   5
#  2 | 2   4   6   8  10
#  etc.
# 
# Hint, to print multiple results on same line try this:
print(f"{result}", end=' ') 
# Where "result" is the multiplication you want to display)
# The "end = ' ' " string causes the automatic carriage return to be overted
# Add an empty print() statement to add a carriage return to move down to the next line.
```
