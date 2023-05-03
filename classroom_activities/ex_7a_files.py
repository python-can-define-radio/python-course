# 1
# Try this. 
# It won't display anything to the screen -- rather, it creates a file.
# Try to find the file it created.
f = open("something_very_unique_file.txt", "w")
f.write("Here are some words.\n")
f.write("More words.")
f.close()

# 2
# Using Python,
# Open the file my_thoughts.txt.
# Write at least 10 separate lines in it.
# Close the file.


# 3
# Using Python,
# Ask the user for name and age.
# Open a file called person_info.txt.
# Write in that file, "___ is ___ years old" (with the name and age filled in).
# Close the file.


# 4
# Try this.
f = open("something_very_unique_file.txt", "r")
contents = f.read()
print(contents)
f.close()


# 5
# When opening a file in Python, if you don't specify a mode, Python will default to 'read' mode ('r'). 
# So, this is equivalent to the previous example:
f = open("something_very_unique_file.txt")
contents = f.read()
print(contents)
f.close()


# 6
# The 'write' mode ('w') will create a new file if the specified file does not exist, or overwrite the contents of the file if it does exist.
f = open("yay_new_file.txt", "w")
f.write("Here are some words for you.")
f.close()

# Now let's read the file
f = open("yay_new_file.txt")
contents = f.read()
print(contents)
f.close()

# Now write into the file again but with different text
f = open("yay_new_file.txt", "w")
f.write("I overwrote those words.")
f.close()

# Now let's read the file again for proof that the original text was overwritten.
f = open("yay_new_file.txt")
contents = f.read()
print(contents)
f.close()

