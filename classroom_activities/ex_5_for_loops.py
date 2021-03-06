# 1
# Try this:
elements = ["water", "earth", "fire", "air"]
for el in elements:
    print(el)

# 2
# Write a `for` loop that prints every item in this list.
thelist = ["water", "chair", "mug", "mouse"]


# 3
# Given this list,
thelist = ["Sam", "Lisa", "Micha", "Dave"]
# Write a `for` loop that outputs
# Hello Sam
# Hello Lisa
# etc.


# 4
# Try this:
word = "Hello world"
for letter in word:
    print(f"The letter is {letter}")


# 5
# Modify the previous example so it asks the user for a string (rather than only using “Hello world”).


# 6
# Modify the previous example so it outputs each letter from the user input followed by “!”. For example:
# H!
# e!
# l!
# l!
# o!


# 7
# For each of the following numbers, display “Half of __ is ___”. For example, “Half of 21 is 10.5”
numbers = [21, 40, 32, 10, 8, 3]


# 8
# Try this:
for num in range(1,5):
    print(num)



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
# Construct the following pattern using a `for` loop. Let the user specify how many rows to print.
# A
# AA
# AAA
# AAAA


# 15
# Given this list,
temps_in_F = [90, 47, 82, 68, 100, 30, 25, 40]
# Display each temperature.


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
