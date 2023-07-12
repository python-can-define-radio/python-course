# Display "Hello world" to the screen
print("Hello world")

# Ask the user for input and display it
thename = input("What is your name? ")
print(f"Hello {thename}")

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

## The next six are "boolean operators".
## They are most often used in the context of an if statement or while statement.
## Some say that booleans are used "to represent truth", but
## I think a better description is to say they are values that can only be True or False.

## The double equals is used to check if two values are equal (that is, to check if they are the same).
are_same = x == y
print(are_same)

## The exclaimation-point-equals is used to check if two values are not equal (that is, to check if they are different).
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
