# 1
# Prompt the user for a string. Print the last three characters using string indexing.


# 2
# Modify the previous question to print “Mike” if the last three characters are MHz, and “Golf” if the last three characters are GHz.
# If the last three are neither of these, print “No match”.


# 3
# Prompt the user for a string. Print all of the characters EXCEPT the last three characters.


# 4
# Prompt the user for a number with MHz. (example input: 2463 MHz.) Print the numerical part.
# You can use split or string indexing. Here's how split works:  
# x, y = "hello world".split() 
# print(x)
# print(y)


# 5
# Modify the previous question so that it converts the given number from MHz to GHz.


# 6
# Prompt the user for a string that contains letters and numbers. Print only the number digits. Hint: use isnumeric. Look up how that function works, then ask for help as needed.


# 7  (challenge question)
# Prompt the user for a word, then display it reversed.
# (There's a built-in Python function for reversing things calld `reversed`, 
#  but you must use `join` with it.)


# 8
# Try this:
x = input("Type some words, and type extra space at the beginning or end.").strip()
print(f"I have removed the extra space. You typed... {x}")


# 9
# Using .strip() and .lower(), ask the user for a name, and check if the name is in a list of allowed usernames.


# 10
# Make a Caesar Cipher.


# 11
# Make Tic Tac Toe.


# 12
# Do the Matplotlib tutorial.
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# or try the matplotlib lesson here: https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch02_Basics/012_matplotlib.md



# 20
# As an exercise, make the Wordle game: https://www.nytimes.com/games/wordle/index.html
# (Note: this is only an educational exercise; please do not infringe on their rights.)

# You'll most likely want to use the `in` keyword:
if "e" in "hello":
    print("The letter e is in the word hello.")
