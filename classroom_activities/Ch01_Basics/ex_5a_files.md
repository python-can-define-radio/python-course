## File Manipulation

```python3 
# 1
# Try this. 
# It won't display anything to the screen -- rather, it creates a file.
# Try to find the file it created.
f = open("something_very_unique_file.txt", "w")
f.write("Here are some words.\n")
f.write("More words.\n")
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
# The 'write' mode ('w') will create a new file if the specified file does not exist,
# or overwrite the contents of the file if it does exist.
f = open("yay_new_file.txt", "w")
f.write("Here are some words for you.\n")
f.close()

# Now let's read the file
f = open("yay_new_file.txt")
contents = f.read()
print(contents)
f.close()

# Now write into the file again but with different text
f = open("yay_new_file.txt", "w")
f.write("I overwrote those words.\n")
f.close()

# Now let's read the file again for proof that the original text was overwritten.
f = open("yay_new_file.txt")
contents = f.read()
print(contents)
f.close()


# 7
# If you want to be more cautious, you can use "x" instead of "w", 
# which will give an error if the file already exists (rather than overwriting it).
f = open("yay_new_file.txt", "x")
f.write("Words to put in the file\n")
f.close()


# 8
# If you want to write at the end of a file ("append"), you can use "a".
f = open("yay_new_file.txt", "a")
f.write("This will write at the end of an existing file.\n")
f.close()


#####################################
## Advanced (optional) topics below this line.
#####################################

# 9
# An example of dealing with large files.

import random

f = open("your_filename_here.txt", "w")
for unusedCounter in range(10000000):
    rnum = random.random() * 10
    f.write(f"{rnum}\n")
f.close()


## RAM-Efficient way
f = open("your_filename_here.txt", "r")
for line in f:
    # Alternatively, could use `if "3.14" in line:` to match anywhere in the line
    # ...but we know in this context that it will be at the beginning of the line
    if line.startswith("3.14"):
        print(line)
f.close()


## RAM-Inefficient way
# f = open("your_filename_here.txt", "r")
# contents = f.read()
# lines = contents.splitlines()
# for line in lines:
#     if line.startswith("3.14"):
#         print(line)
# f.close()


# 10
# An example of reaching the maximum-number-of-open-files,
# i.e., why you should close files after using them.
# WARNING: you may have to reboot your computer after running this.
# (No permanent damage as far as I am aware.)

filehandlelist = []
 
for count in range(0, 500000):
    filename = f"file_num_{count}.txt"
    f = open(filename, "w")
    filehandlelist.append(f)
```
