# Display "Hello world" to the screen
print("Hello world")

# Ask the user for input and display it
thename = input("What is your name? ")
print(f"Hello {thename}")

# More ways to use a variable in a print statement
print("Hello", thename)
print("Hello {}".format(thename))
print("Hello" + thename)     # This works if thename is a string
print("Hello %s" % thename)  # This approach was more common in Python 2

# Add
x = 5
y = 3
added = x + y
print(added)

# When working with strings, the + sign is used for concatenating
a = "You say..."
b = "Goodbye"
together = a + b
print(together)
