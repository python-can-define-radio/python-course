# Change your current directory
cd newLocation

# List what's in this directory
ls

# Write "Hello world" to a file, overwriting whatever is there
echo "Hello World" > myfile.txt

# Write "Hello world" to the end of a file
echo "Hello World" >> myfile.txt

# Copy file
cp original.txt new.txt

# Make directory
mkdir mydirectoryname

# Move file; also used for renaming
mv original.txt new.txt

# Display file
cat myfile.txt

# Display multiple files, concatenated  (this is the origin of the name cat)
cat somefile.txt anotherfile.txt

# Display contents in a tree
tree

# Display file with ability to scroll using arrow keys.
# Press q to quit
less myfile.txt

# ------------------------------------
# below is a semi-overlapping list that I plan to de-dupe

Terminal commands
- cd: change directory

   Example:
    ~/Desktop/mystuff$ cd food
    ~/Desktop/mystuff/food$

   Example:
    ~/Desktop/mystuff/food$ cd ..
    ~/Desktop/mystuff$

   
- mkdir: make directory (folder)

- help: provide help on a command

   Example:
    $ help cd

- info: provide info on a command 
  (useful when help doesn't work)
  Press q to quit when you're done.

   Example:
    $ info cd

- tree

- echo: Can be used for displaying to the screen, OR for writing to files.

   Example (display to screen):
    $ echo "hello world"

   Example (write to file):
    $ echo "hello world" > myfile.txt

   Example (append to file):
    $ echo "hello world" >> myfile.txt


- ls: List directory contents

- touch: create an empty file

- mv: move or rename

   Example (relocate):
    $ touch a.txt
    $ mkdir stuff
    $ ls
    a.txt  stuff
    $ mv a.txt stuff
    $ ls
    stuff


   Example (rename):
    $ ls
    thing.txt  other.txt
    $ mv thing.txt newname.txt
    $ ls
    newname.txt  other.txt

- cat: Display file contents
