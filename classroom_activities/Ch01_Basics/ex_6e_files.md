# File Manipulation

ℹ️ This material coincides with material from python slideshow D (slides 31-37).

### Exercises

```python3 
## 1
## Try this. 
## It won't display anything to the screen -- rather, it creates a file.
## Try to find the file it created.
f = open("something_very_unique_file.txt", "w", encoding="utf-8")
f.write("Here are some words.\n")
f.write("More words.\n")
f.close()
## Memo: Within the 'open()' command, the "w" invokes the "write" mode, which creates a new file if the specified file does not exist,
##       or overwrite the contents of the file if it does exist.


## 2
## Using Python,
## Open the file my_thoughts.txt.
## Write at least 10 separate lines in it.
## Close the file.


## 3
## Using Python,
## Ask the user for name and age.
## Open a file called person_info.txt.
## Write in that file, "___ is ___ years old" (with the name and age filled in).
## Close the file.


## 4
## Try this.
f = open("something_very_unique_file.txt", "r", encoding="utf-8")
contents = f.read()
print(contents)
f.close()


## 5
## When opening a file in Python, if you don't specify a mode, Python will default to 'read' mode ('r'). 
## So, this is equivalent to the previous example:
f = open("something_very_unique_file.txt", encoding="utf-8")
contents = f.read()
print(contents)
f.close()

## 5a
## As with any Python string, you can use a variable instead of
## typing the string directly.
## Copy and modify the previous example to do the following:
## - Ask the user for the name of the desired text file.
## - Display "Reading the file ____." (fill the blank with the user-defined filename.)
## - Display the contents of that file.
#######################
## INSTRUCTOR CHECK
#######################
```

Note: It's [considered good practice](https://pylint.pycqa.org/en/latest/user_guide/messages/warning/unspecified-encoding.html) to specify the encoding of a file when reading or writing. It's not strictly necessary, but omitting the encoding can cause issues with special characters on the Windows OS, so we are following the recommended practice.

```python3
## 6
## Another example of writing to a file.  If the file exists, it will be over-written.
f = open("yay_new_file.txt", "w", encoding="utf-8")
f.write("Here are some words for you.\n")
f.close()

## Now let's read the file
f = open("yay_new_file.txt", encoding="utf-8")
contents = f.read()
print(contents)
f.close()

## Now write into the file again but with different text
f = open("yay_new_file.txt", "w", encoding="utf-8")
f.write("I overwrote those words.\n")
f.close()

## Now let's read the file again for proof that the original text was overwritten.
f = open("yay_new_file.txt", encoding="utf-8")
contents = f.read()
print(contents)
f.close()


## 7
## If you want to be more cautious, you can use "x" instead of "w", 
## which will give an error if the file already exists (rather than overwriting it).
f = open("yay_new_file.txt", "x", encoding="utf-8")
f.write("Words to put in the file\n")
f.close()


## 8
## If you want to write at the end of a file ("append"), you can use "a".
f = open("yay_new_file.txt", "a", encoding="utf-8")
f.write("This will write at the end of an existing file.\n")
f.close()
```


### Optional exercises

<details><summary>Expand here for additional content.</summary>.

This is an example of how to work with large files. 

Make sure you have at least a few hundred MB of free hard drive space before running these.

```python3
## 9a
## Try this. It will create a file called your_filename_here.txt.
import random

f = open("your_filename_here.txt", "w", encoding="utf-8")
for unusedCounter in range(10000000):
    rnum = random.random() * 10
    f.write(f"{rnum}\n")
f.close()


## 9b
## This is an example of a RAM-Efficient way to process the file.
f = open("your_filename_here.txt", "r", encoding="utf-8")
for line in f:
    # Alternatively, could use `if "3.14" in line:` to match anywhere in the line
    # ...but we know in this context that it will be at the beginning of the line
    if line.startswith("3.14"):
        print(line)
f.close()


## 9c
## This does the same as the previous example, but
## is RAM-Inefficient because it loads the entire file
## into RAM rather than just reading one line at a time.
f = open("your_filename_here.txt", "r", encoding="utf-8")
contents = f.read()
lines = contents.splitlines()
for line in lines:
    if line.startswith("3.14"):
        print(line)
f.close()
```

⚠️ Warning: the example below creates thousands of files on your hard drive!

```python3
## 10
## An example of reaching the maximum-number-of-open-files,
## i.e., why you should close files after using them.
## WARNING: you may have to reboot your computer after running this.
## (No permanent damage as far as I am aware.)

import os
from pathlib import Path

rootdir = Path("many_files_are_in_here")
os.mkdir(rootdir)
filehandlelist = []
for count in range(0, 500000):
    filename = rootdir / f"file_num_{count}.txt"
    f = open(filename, "w", encoding="utf-8")
    filehandlelist.append(f)
```
</details>
