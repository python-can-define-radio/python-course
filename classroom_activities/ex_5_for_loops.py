# 1
# Try this:
elements = ["water", "earth", "fire", "air"]
for element in elements:
    print(element)

    
# 1b
# Try this:
colors = ["red", "orange", "yellow"]
for color in colors:
    print(color)
    
    
# 2
# Write a `for` loop that prints every item in this list.
household_items = ["water", "chair", "mug", "mouse"]


# 3 
# Try this:
names = ["Sam", "Lisa", "Micah", "Dave"]
for name in names:
    print(f"Hello {name}. Welcome to the Python course.")

    
# 3b
# Copy and modify the previous example like so:
# for each name, display "Have a good day, ____. I hope you enjoyed experimenting with python."
# (Fill in the blank with the name.)


# 4
# Try this:
ages = [26, 37, 55, 10, 5]
for age in ages:
    print(f"One of the people in my list is {age} years old.")
    print(f"In two years, that person will be {age + 2} years old.")


# 4b
# Copy and modify the previous example so that for each age,
# it displays "5 years ago, that person was ___ years old."


# 5
# For each of the following numbers, display “Half of __ is ___”. For example, “Half of 21 is 10.5”
numbers = [21, 40, 32, 10, 8, 3]


# 6
# As you've seen, you can use a `for` loop with lists.
# You can also use a `for` loop with a string.
# For example, try this:
phrase = "Hello world"
for letter in phrase:
    print(f"The letter is {letter}")


# 7
# Copy and modify the previous example so it asks the user for a string (rather than only using "Hello world").


# 7b
# Copy and modify the previous example so it outputs each letter from the user input followed by "!". For example:
# H!
# e!
# l!
# l!
# o!



# 8
# You can also use a `for` loop with a range.
# Try this:
for num in range(1,5):
    print(num)
# Note: You'll notice it always omits the final number.
# It may seem odd, but it was an intentional decision in the design of Python (and other languages).
# Why? The short explanation  is that it helps avoid off-by-one errors.
# Ask an instructor if you're curious.
# Here are some further explanations:
#   https://howdoesinternetwork.com/2015/numbers
#   https://howdoesinternetwork.com/wp-content/uploads/E.W.-Dijkstra-Archive-Why-numbering-should-start-at-zero-EWD-831-transcript.html
#   https://stackoverflow.com/questions/4504662/why-does-rangestart-end-not-include-end


# 9
# Modify the previous example to print the numbers 1 to 6.


# 10
# For each of the integers 1 to 5, print that number squared.
# Use the range function.
# (In other words, the lists [1, 2, 3, 4, 5] and [1, 4, 9, 16, 25] should not appear in your code.)


# 11
# Modify the previous example to allow the user to specify the highest number rather than stopping at 5.
# Ex:
# Highest number?  (user types 4)
# 1
# 4
# 9
# 16


# 12
# Try this:
print("Hello"*3)


# 13
# Modify the previous example to ask the user how many "Hello"s to print.


# 14
## (challenge question; can skip)
# Construct the following pattern using a `for` loop. Let the user specify how many rows to print.
# A
# AA
# AAA
# AAAA


# 15
# Try this.
temps_in_F = [90, 47, 16, 82, 68, 100, 30, 25, 40]
for temp in temps_in_F:
    print(f"The temperature was {temp}")

    
# 15b
# Try this.
temps_in_F = [90, 47, 16, 82, 68, 100, 30, 25, 40]
for temp in temps_in_F:
    print(f"The temperature was {temp}")
    if temp > 90:
        print("That's hot.")


# 16
# Modify the previous question to display the temperature and display whether it is above or below freezing.


# 17
# Try this:
x = input("Say a word: ")
if x.endswith("s"):
    print("That ends with an 's', so it might be plural.")
print("That's all I have to say.")


# 18
# Modify the previous example so that if the user input ends with "day",
# then the computer will display "I think that's a day of the week."



# 19
# Try this:
fruits = ["strawberry", "raspberry", "blueberry", "grape", "mango", "melon"]
count = 0
for fr in fruits:
    if fr.endswith("berry"):
        count += 1
print("I've finished counting the fruits.")
print(f"There were {count} that ended with berry.")

# 20
# Using `startswith` (which works quite similarly to endswith),
# count how many of the fruits start with 'm'.
# Then display the count.


# 21
# Given this list, count how many temperatures are above freezing.
# Display the count.
temps_in_F = [90, 47, 82, 68, 100, 30, 25, 40]



# 22
# Copy and modify the previous example to show the user how many
# temperatures are above freezing and how many are below freezing.


# 23
# Modify the earlier example so it outputs the indices of the letters before the letters.
# Hint: One way to do this is using enumerate -- look up examples of the enumerate function in python.

# Example output:

# 0: H!
# 1: e!
# 2: l!
# 3: l!
# 4: o!
# Etc.


# -- Introduction to the next few questions --
# Your spectrum analyzer is logging which frequencies have shown activity.
# It makes a note of the center frequency of each burst of activity.
# Here’s what it has recorded (units are MHz):
freqs = [2403.6, 101.3, 90.1, 5.2, 2410.2, 3.7]

# 24
# Using a loop, print each frequency, and then print whether it is
# in the Wi-Fi range, the FM Radio range, or Neither Wi-Fi nor FM.


# 25
# Modify the previous example to count how many frequencies were in each category.
# At the end of the program, print the count for each category.


# 26
# A report is being produced which only shows detected Wi-Fi frequencies.
# Make a copy of the previous program that only prints the Wi-Fi frequencies from the list.


# 27
# After having read the report, someone wants to know where in the list that the Wi-Fi
# frequencies occur. Make a program that prints both Wi-Fi frequencies and their indices.
# You'll most likely want to use the enumerate function.

# Expected output:
# 2403.6 MHz: index 0
# 2410.2 MHz: index 4


# 28
# Some of the audience of the report is unfamiliar with MHz.
# Modify one (any one) of the above spectrum-related questions
# to allow the user to choose if they want to see the results in MHz or GHz.
# Then print the frequencies using the chosen unit.


# 29
# Someone now wants a program to convert between MHz and GHz.
# The person wants to be able to type everything in one prompt, for example,

#   What would you like to convert? 3445 MHz
#   That is 3.445 GHz.

# Convert appropriately from MHz to GHz or vice versa using input from a single prompt.
# Note 1: the following exercise provides a useful hint.
# Note 2: You can assume the user enters valid data, or, for a challenge, check for data validity.

# 30
# Try this:
userdata = input("Enter two numbers, separated by a space.")
a, b = userdata.split()
print(f"First number: {a} and second number: {b}")


# 31
# Try this:

# Hint: The following five exercises provide stepping stones toward this goal. Also,
# this exercise doesn't require a loop.
