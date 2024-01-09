# Some Useful Commands for the Linux Terminal
# NOTE: Some of these examples assume a particular directory or, equivalently, folder structure already exists on the hard drive or 
#       other memory device where you are working while using the Terminal program.

# List what's in your current directory or, equivalently, folder (The location on the hardrive or other memory device.)
# I.e., list the directory's contents.
ls

# Change from your current directory to another
# Example:
cd newLocation 
# NOTE: In place of "newLocation" use a directory name that exists

# Example of cd command and its result:
# Change your current directory
# Example:
cd newLocation

# Example of cd with output:
#    ~/Desktop/mystuff$ cd food
#    ~/Desktop/mystuff/food$
# Example of using the special directory, .., which means "one directory higher than where I am"
#    ~/Desktop/mystuff/food$ cd ..
#    ~/Desktop/mystuff$

# Write "Hello world" to a file, overwriting whatever is there
echo "Hello World" > myfile.txt

# Write "Hello world" to the end of a file
echo "Hello World" >> myfile.txt

# Copy a file
cp original.txt new.txt

# Make a directory, a.k.a, a folder
mkdir mydirectoryname

# The touch command creates an empty file.
touch mynewfile.txt

# The mv command is used for moving and renaming.
# Here's an example of putting a file into a directory:
touch a.txt
mkdir stuff
ls
mv a.txt stuff
ls
cd stuff
ls

# Here's an example of using mv (the move command) to rename something:
mv original.txt new.txt

# Display file
cat myfile.txt

# Display multiple files, concatenated  (This word is the origin of the cat command.)
cat somefile.txt anotherfile.txt

# Display contents in a tree-structured format
tree

# Display file with ability to scroll using arrow keys.
# Press q to quit
less myfile.txt

# ------------------------------------
# Below is a semi-overlapping list that we plan to de-dupe.

# Terminal commands

# - help: provide help on a command

   Example:
    $ help cd

- info: provide info on a command 
  (useful when help doesn't work)
  Press q to quit when you're done.

   Example:
    $ info cd


# - echo: Can be used for displaying to the screen, OR for writing to files.

   Example (display to screen):
    $ echo "hello world"

   Example (write to file):
    $ echo "hello world" > myfile.txt

   Example (append to file):
    $ echo "hello world" >> myfile.txt

