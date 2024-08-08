## Definitions:
#  print()     Displays to screen
#  input()     Asks for user input
#  int()       Convert to an integer
#                (a positive or negative whole number, such as 3, -2, etc).
#                Often used with input.
#  float()     Convert to a float
#                (a number that has a non-whole part, such as 2.5, -3.7, etc).
#                Often used with input.


# Display "Hello world" to the screen
print("Hello world")

# Ask the user for input and display it
thename = input("What is your name? ")
print(f"Hello {thename}")

# Ask the user for a non-whole number (a `float`):
num = float(input("What is your name? "))
print(f"Hello {num}")

# More ways to use a variable in a print statement
# Reminder: a variable is used to store data.
print("Hello", thename)
print("Hello {}".format(thename))
print("Hello" + thename)     # This works if thename is a string
print("Hello %s" % thename)  # This approach was more common in Python 2

# Common operators
x = 5
y = 3
# Add, sum
added = x + y   
print(added)
# subtraction, subtract, minus
subtr = x - y
print(subtr)
# multiply, multiplication, product
mult = x * y
print(mult)
# divide, division, quotient
divi = x / y
print(divi)

# floor division, round-down division
floor_div = x // y
print(floor_div)

## exponent, exponentiation
## Note that the caret symbol (meaning the ^) is NOT used for calculating an exponent in Python.
exponentiated = x ** y
print(exponentiated)

## This one, the remainder operator, is also known as modulus.
## Note that it has nothing to do with percentages!
remainder = x % y
print(remainder)

## The next six operators are "boolean operators".
## They are most often used in the context of an if statement or while statement.
## Some say that booleans are used "to represent truth". (In fact, this is the 
## "correct" definition for boolean on a certain test that we've seen.)
## However, here's a better description, from the Mozilla Developer Network (MDN):
## "A Boolean is a logical data type that can have only the values True or False."

## The double equals is a comparison operator which is used to check if two values are equal (that is, to check if they are the same).
are_same = x == y
print(are_same)

## The exclaimation-point-equals is a comparison operator used to check if two values are not equal (that is, to check if they are different).
are_different = x != y
print(are_different)

greater_than = x > y
print(greater_than)

greater_than_or_equal_to = x >= y
print(greater_than_or_equal_to)

less_than = x < y
print(less_than)

less_than_or_equal_to = x <= y
print(less_than_or_equal_to)

someNumber = 10
## After running this, someNumber will contain the number 12.
someNumber += 2

## You can do the same for many other operators:
someNumber -= 3
someNumber *= 3
someNumber /= 3

# When working with strings, the + sign is used for concatenating
a = "You say..."
b = "Goodbye"
together = a + b
print(together)

# Another common string operation is lowercasing:
a = "Something With Capitalization"
b = a.lower()

# .lower() is often used in if statements.
# Remember the parentheses! ()
response = input("Say something: ")
if response.lower() == "no":
    print("You said no, or No, or...")
else:
    print("Ok")
