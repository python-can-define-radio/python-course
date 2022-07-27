#### Some useful resources:
### Background info about "Why the terminal": 
###  - ubuntu.com/tutorials/command-line-for-beginners#2-a-brief-history-lesson
###  - askubuntu.com/questions/106039/so-what-is-the-advantage-of-using-the-terminal
### Tutorials:
###  - The one we'll be using: ubuntu.com/tutorials/command-line-for-beginners
###  - Another: linuxsurvival.com


### Preliminaries:
### Make a directory on the Desktop with your name. No spaces :-)
### Inside, create and open a file called notes.txt.
### Use it to make notes about what the commands do.


## 1
## First, run these. (Together as a class)
cd ~
ls
cd Desktop
ls
mkdir mystuff
ls
cd mystuff
ls
touch a.txt
ls
touch b.txt
ls


## 2 
## After running those commands,
##  - Use the GUI file browser to look at the files you just created.
##  - Open the two text documents and add some content. Save the files.


## 3
## We're going to display the files in the terminal:
cat a.txt
cat b.txt


## 3b
## You can display everything in that directory that ends with txt:
cat *.txt


## 4
## And now we'll create another file, and this time, we'll write to it:
echo "Words are going in this file" > c.txt


## 5
## Verify that the previous command created a file with words in it.


## 5b
## Let's dissect the previous command a little.
## Try this:
echo "Hello"
## You'll see that it simply displays what you wrote on the screen.
## echo is primarily useful in scripting, but in this class, we'll be
## using it to write to files.
## When you write this...
##    echo "something" > somefile.txt
## ... It's doing what's called output redirection.
## That means the "something" which normally gets displayed on the screen
## is being redirected into a file.
## You can do that with other commands.
## For example, this would make a file called combinedstuff that contains
## the contents of all of the txt files in a directory.
##    cat *.txt > combinedstuff
## 


## 6
## Using the terminal:
## 6a: Create a file called d.txt, with the (non-empty) content of your choice.
## 6b: Create two more files with names of your choice (no spaces), and with the content of your choice.


## 6b
## Try this.
mkdir foods
mkdir drinks


## 6c
## Use cd to go inside the foods directory that you just created.
## Make a file called sandwich.txt. Inside the file should be a description of a sandwich.

## 6d
## Now we want to get out of the foods directory.
## There's a special name for "one directory higher than where I am":
cd ..

## 6e
## Use cd to go inside the drinks directory.
## Make a file called herbalTea.txt. Inside the file should be what you think about herbal tea.

## 6f
## Make another directory. Put two files in it with the names and contents of your choice.

## 7
## Here's how you append to a file. When might that be useful?
echo "This is a new bit of text" >> a.txt


## 8
## First run these.
cd /
cd tmp
mkdir otherstuff
cd otherstuff


## 9
## Keep your terminal open.
## Also, open the GUI file browser, and navigate to the same location.
## One way to do this:
## - Open the GUI file browser:
## - Hold "Alt" on the keyboard, and press the Up arrow multiple times
## - Go inside the "tmp" directory
## - Go inside the "otherstuff" directory


## 10
## Inside of the otherstuff directory,
## make the following folder structure using the terminal.
## Put the words of your choice inside of the txt files.
## .
## └── house
##     ├── smallstuff
##     │   ├── pencil.txt
##     │   ├── marker.txt
##     │   └── eraser.txt
##     └── furniture
##         ├── chair.txt
##         ├── table.txt
##         └── desk.txt
