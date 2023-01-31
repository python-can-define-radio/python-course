
The goal of the current lesson is to familiarize new students with the "Terminal" program of the Linux operating system (OS).

### Background Information:
This exercise is developed based on the Ubuntu distribution of the Linux OS, but should be applicable for other distributions as well. Linux includes several pre-installed programs or applications, commonly called "Apps".  One such pre-installed program is the Terminal, which is a text-based user interface for interacting with the OS itself, with storage devices (e.g., a hard drive, CD/DVD drive, or flash drive), and with the internet.  The Terminal program is also called the "command-prompt", the "shell", and the "console".  (Further details: for older Unix computer systems, the terms "terminal" and "console" referred to a physical piece of equipment.  Within the Linux OS, they refer to software providing similar functionality). 


### Some useful resources:
`(Suggestion: When using a web-link, Right-Click with your mouse and select "open in new window".)`
- Background info about "Why the terminal": 
  - https://ubuntu.com/tutorials/command-line-for-beginners#2-a-brief-history-lesson
  - https://askubuntu.com/questions/106039/so-what-is-the-advantage-of-using-the-terminal


### Exercises
Preliminary Tasks:  (Instructions follow)
- Make a directory on the Desktop with your name. No spaces :-)
- Inside, create and open a file called notes.txt.
- Use it to make notes about what the commands do.

```sh
## 1
## First, run these.
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
```

Now Try These:
```sh
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


## 6g
## You can view the structure of your files and directories like this:
tree
## Notice how the output changes depending on your current working directory:
cd ..
tree
cd ..
tree


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
## Everything that ends in .txt should be a file, NOT a directory.
## Put the words of your choice inside of the txt files.
## An easy way to verify this is by running the `tree` command that you just learned.
## 
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


## 11
## You can evaluate a command within another command:
echo "Right now the date and time is $(date)" >> myfile.txt 


## 12
## Try this. It displays the path of the "working directory", that is, the one where your terminal is focused.
pwd


## 13
## When doing cd, you can do multiple steps like this:

## Long way:
cd ~
cd Desktop
cd mystuff

## Short way:
cd ~/Desktop/mystuff


## 13b
## Use cd to change your directory back to /tmp/otherstuff .


## 14
## Use output redirection, that is, the > character, to write the current working directory to a file.


## 15
## Here's how to copy a file, and then display it using cat.
## Note that this will only work if you start by chanding your directory (cd) to where pencil.txt is located.
cp pencil.txt writing_tool.txt
cat writing_tool.txt


## 16
## Here's how to remove a file. Be very careful, as it skips the trash can, and does not confirm before removing! 
## How to be careful: 
##  - Avoid wildcards (the * character) with rm
##  - Use cat to view the file before removing it
rm writing_tool.txt


## 17
## Try this. You can see that grep displays all occurences of the word "view".
## Don't forget the asterisk in the grep command. The asterisk means "everything in my current directory".
cd /tmp/otherstuff/house/smallstuff
echo "used for viewing items." > eyeglasses.txt 
echo "a beautiful view, I would say." > mountains.txt 
grep view *


## 17b
## To move something, use mv:
cd /tmp/otherstuff/house
echo "A comfortable place to sit." > couch.txt
mv couch.txt furniture


## 17c
## You can also use the special two dots that we saw when we were using cd:
cd /tmp/otherstuff/house/smallstuff
ls
mv mountains.txt ..
ls
cd ..
ls


## 17d
## Make a directory called "scenery", and move mountains.txt into it.


## 18
## Make a few example text files for yourself. Be sure to include the word "explore" in some of the files.
## Then, use grep to find occurences of the word "explore" in these files.


## 19
## grep can also search within subdirectories using the -r flag.
## Try this:
cd /tmp/otherstuff/
grep -r explore *


## 20
## Use grep to search for the letter "a" in all files in all subdirectories in /tmp/otherstuff.


## 21
## Copy and modify the previous example so that it uses output redirection to write grep's output to a file.


## 22
## To look back on what commands you've used, you can run this:
history

```

At this point, if you finish before the rest of the class, or if you'd like more practice with the terminal, start working on one of these tutorials:

  - https://ubuntu.com/tutorials/command-line-for-beginners
  - https://linuxsurvival.com
