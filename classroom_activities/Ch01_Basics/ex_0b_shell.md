# Shell/Bash/Terminal/Command Prompt

The goal of the current lesson is to familiarize new students with the "Terminal" program of the Linux operating system (OS).  

ℹ️ This material coincides with material from python slideshow A (slides 1-20).  

### Background Information:
<details><summary>Expand here</summary>

This exercise is developed based on the Ubuntu distribution of the Linux OS, but should be applicable for other distributions as well. Linux includes several pre-installed programs or applications, commonly called "Apps".  One such pre-installed program is the Terminal, which is a text-based user interface for interacting with the OS itself, with storage devices (e.g., a hard drive, CD/DVD drive, or flash drive), and with the internet. The Terminal program is also called the "command-prompt", the "shell", and the "console".  (Further details: for older Unix computer systems, the terms "terminal" and "console" referred to a physical piece of equipment.  Within the Linux OS, they refer to software providing similar functionality).

</details>

### Some useful resources:
<details><summary>Expand here</summary>

- Background info about "Why the terminal": 
  - https://ubuntu.com/tutorials/command-line-for-beginners#2-a-brief-history-lesson
  - https://askubuntu.com/questions/106039/so-what-is-the-advantage-of-using-the-terminal
- A list of several Terminal commands: https://www.digitalocean.com/community/tutorials/linux-commands
- (See also links to tutorials at bottom of this page.)

</details>

### Notes: 
- The examples below assume you have run the `student_config_script.sh` file as described in the [Preliminaries lesson](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch01_Basics/ex_0a_preliminaries.md)  That "script" program file adds several text files used in the current lesson and adds other features.
- In the text below, a pair of pound symbols (##) introduces instructions or a comment for you, the student.
- Commands to be entered in Linux Terminal window are written without any such prefix.
- Press the {enter} key after each command line. 
- If you would like to clear the terminal at any point, press `Ctrl + L` or type the `clear` command.
- While in the Linux command line, `Ctrl + C` is used to send a SIGINT (signal interrupt) signal, which cancels or terminates the currently-running program.

### Exercises

```sh
## 1 
## - Using the Graphical User Interface (GUI) file browser, open the folder "term_example_files" on the Desktop.
##   This folder should have been created by the initial setup script that you ran in the Preliminaries lesson.
## - Open the files and folders to see what is in them.


## 2
## Now that we've explored the contents using the graphical interface with which you are familiar,
##     we're going to explore the folder structure and files using the CLI (Command Line Interface),
##     a.k.a., the Terminal program.
## First, open an instance of the Terminal by one of several methods:
##     (a) In a GUI files browser, in the right window pane, right-click on white space and select "Open in Terminal".
##     (b) On the computer's Desktop, right-click and select "Open in Terminal".
##     (c) Press the "super" key & begin typing "terminal".  When the appropriate icon appears, click on it.
##     (Can't find the "super" key? See https://itsfoss.com/super-key/ )
## NOTE: As you type commands or names of folders or files in the CLI (the Terminal),
##     you can SAVE TIME by pressing the Tab key to autofill the rest of a command or name.
##     For example, you can type cd ~/Des (the first three letters of "Desktop") and then press Tab, and the OS
##     will add the remainder of that folder name. If this autofill feature is not working, let an instructor know.
## Now, run these commands:  (Remember, press the Enter key after each line.)
cd ~
pwd
## What happened?
## What does the tilde ~ represent?
## Do this.
cd Desktop
pwd
cd term_example_files
pwd
cd animals
pwd
## Notice the change in your location when you run pwd.
## We can do these commands seperately like the example above or together like the example below.
cd ~
cd Desktop/term_example_files/animals/
## Lets add another command
ls
## What happened?

```

<details><summary>Expand here and read if you do not understand cd, ls, or pwd.</summary>

You've now used three commands: `cd`, `ls`, and `pwd`. The first command, `cd`, stands for "<b>c</b>hange <b>d</b>irectory". The second command, `ls`, stands for "<b>l</b>i<b>s</b>t". Whenever you type `ls`, the terminal displays a list of files. The files that are displayed by `ls` vary according to your current "working directory".

A "working directory" is the directory (a.k.a. folder) that you are currently interacting with --
any commands you run will be run in that directory. If you list files, it lists the files _in that directory_. If you create a file, it creates it _in that directory_. (There will be exceptions, but we'll handle those later.)

The third command, `pwd`, stands for "<b>p</b>rint <b>w</b>orking <b>d</b>irectory". Notice how it changed every time you changed your directory using `cd`:

- After running `cd Desktop`, when you ran `pwd`, it displayed `/home/yourusername/Desktop`.
- After running `cd term_example_files`, when you ran `pwd`, it displayed `/home/yourusername/Desktop/term_example_files`.

You may wonder why `pwd` does not show `~/Desktop/term_example_files`. The reason: `~` (the tilde character) is a GNU/Linux abbreviation for your home directory, which is normally `/home/yourusername`. So, if your user name is `bob.smith`, then `~` means `/home/bob.smith`.

</details>

Let's get some practice:

```sh
## 3a
## Try this.
cd ~
ls
cd Desktop
ls
cd vehicles
## Note: the `cd vehicles` command will give an error. Why?
```

<details><summary>Expand here for the answer.</summary>

The command `cd ~` means "change directory (`cd`) to my home directory (`~`)".

When we used the command `cd vehicles` it gave this error: `bash: cd: vehicles: No such file or directory`. Let's break this down:

- `bash`: We are using `bash` as our "shell". There are various available shells with different features, but in this class, we'll just use bash.
- `cd`: The terminal is letting you know that `cd` is the command that failed.
- `vehicles: No such file or directory`: Before trying to change your directory, `cd` checks if the desired destination exists. In this case, it looked for `vehicles` in your current working directory, which was the Desktop. However, `vehicles` does not exist on the Desktop; it's inside `term_example_files`.

</details>

```sh 
## 3b
## Change your current directory to the animals directory.
## You may wish to use the command `cd ~` first.


## 3c
## Change your current directory to the vehicles directory.
```

You may have noticed that it's tedious to have use `cd ~` to go back to your home directory every time you want to go into another directory. There is a special location, `..`, that means "the parent directory of this directory".

```sh
## 4
## Try this. Notice what happens when you run `cd ..`.
cd ~
cd Desktop
cd term_example_files
cd ..
## What did the cd .. command do?
pwd
## You can also navigate multiple levels at once this way.
cd term_example_files/animals
pwd
cd ../..
pwd
## See how it moved two levels up.
```

You may wonder why `cd ~` works regardless of where you run it. Let's distinguish between two types of paths:

- **Relative Paths** are called that because they are relative to your current working directory.
  - Examples:
    - `cd animals`
    - `cd ../vehicles`
    - `cd term_example_files/plants`
    - `cd Desktop/term_example_files/plants`
- **Absolute Paths** do not depend on your current working directory. Any path that begins with a `~` or a `/` is an absolute path.
  - Examples:
    - `cd ~/Desktop/term_example_files/plants`
    - `cd ~/Desktop/term_example_files/animals`
    - `cd /home/someusername/Desktop/term_example_files/animals`  _(Note: This won't work unless you change "someusername" to your username.)_

Examples:

| Relative | Absolute |
|-----------|--------|
| cd animals | cd ~/Desktop/term_example_files/animals |
| cd vehicles | cd ~/Desktop/term_example_files/vehicles |

Some further examples are below.

```sh
## 5
## Try this. Does this example use an absolute path or a relative path? (answer: absolute)
cd ~/Desktop/term_example_files/animals


## 6
## Try this. Notice that `cd ~` uses an absolute path, but
## the other three `cd` commands use relative paths.
## 
cd ~
cd Desktop
cd term_example_files
cd animals
```

Absolute paths are useful because they work regardless of your current directory.  
Relative paths are useful because of their brevity and because they work even if the parent directories change.

Now that we know how to change directories, let's display the contents of some files.

```sh
## 7
## Try this. Remember to press Tab often to try to save keystrokes.
cd ~/Desktop/term_example_files/animals
ls
cat monkey.txt
```

The command `cat` displays the contents of one or more files. 

```sh
## 8
## Try displaying the contents of "dog.txt" using the cat command.


## 9
## Try this:
cat monkey.txt dog.txt
```

You'll see that if you `cat` more than one file, it displays all of the contents chained together. The fancy name for this is "concatenate". "Concatenate" comes from the Latin word _catena_, which means "chain". We are "concatenating" the files `monkey.txt` and `dog.txt` (displaying them "in a chain").

Incidentally, this is the origin of the name `cat`.

```sh
## 10
## Use `cat` to display the contents of all of the text files in the "animals" directory.


## 11
## Use `cd` to change directories to "term_example_files".
## Then use `ls` to list the contents of that directory.
```

```sh
## 13
## Do these steps:
## - change directory to the Desktop.
## - change directory to term_example_files.
## - change directory to plants.
## - list what is in that directory.
## - Use `cat` to display the contents of the file "general_info_plants.txt".
## - Use `cd ..` to change out of that directory.
## - change directory to vehicles.
## - change directory to engines.
## - Use `cat` to display the contents of the file "combustion_engines.txt".
```

Now, let's move some files using the `mv` command.

```sh
## 14
## Try this. It will move the file "kangaroo.txt" inside the animals directory.
cd ~/Desktop/term_example_files
ls
mv kangaroo.txt animals


## 15
## Notice that in "term_example_files", there are two files related to Mustangs.
## Use `cat` to display the contents of each.
## Based on the contents, decide which directory each should be moved into
##  (the "animals" directory or the "vehicles" directory).
## Move each file appropriately.
########################
##  INSTRUCTOR-CHECK  ##
########################
```

You can use the aforementioned `..` in the `mv` command too:

```sh
## 16
## Try this. Where is cactus.txt after running these commands?
cd ~/Desktop/term_example_files
cd animals
mv cactus.txt ..
```

You can **c**o**p**y files using the `cp` command, which works just like `mv`, but keeps the original.

```sh
## 17
## Try this. What does it do?
cd ~/Desktop/term_example_files/plants
cp general_info_plants.txt plant_info.txt
```

### If you have reached this point, you can switch to `ex_1a_print_and_inputs`.

## Misc practice (Optional)

<details><summary>Expand here for additional content.</summary>

```sh
## 22
## You can search for all files that have an "a" in their name:
tree -f | grep a

## 23
## You can display everything in a directory that ends with txt:
cat *.txt


## 24
## And now we'll create another file, and this time, we'll write to it:
echo "These words are going into this file" > c.txt


## 25
## Verify that the previous command created a file with words in it.
## (What command allows you to view the contents of a file? Look above.)

## 25b
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


## 26
## Using the terminal:
## 6a: Create a file called d.txt, with the (non-empty) content of your choice.
## 6b: Create two more files with names of your choice (no spaces), and with the content of your choice.


## 26b
## Try this.
mkdir foods
mkdir drinks


## 26c
## Use cd to go inside the foods directory that you just created.
## Make a file called sandwich.txt. Inside the file should be a description of a sandwich.


## 26d
## Now we want to get out of the foods directory.
cd ..


## 26e
## Use cd to go inside the drinks directory.
## Make a file called herbalTea.txt. Inside the file should be what you think about herbal tea.


## 26f
## Make another directory. Put two files in it with the names and contents of your choice.


## 26g
## You can view the structure of your files and directories like this:
tree
## Notice how the output changes depending on your current working directory:
cd ..
tree
cd ..
tree


## 27
## Here's how you append to a file. When might that be useful?
echo "This is a new bit of text" >> a.txt


## 28
## First run these.
cd /
cd tmp
mkdir otherstuff
cd otherstuff


## 29
## Keep your terminal open.
## Also, open the GUI file browser, and navigate to the same location.
## One way to do this:
## - Open the GUI file browser:
## - Hold "Alt" on the keyboard, and press the Up arrow multiple times
## - Go inside the "tmp" directory
## - Go inside the "otherstuff" directory


## 30
## Inside of the otherstuff directory,
## make the following folder structure using the terminal.
## Everything that ends in .txt should be a file, NOT a directory.
## Put the words of your choice inside of the txt files.
## An easy way to verify this is by running the `tree` command that you just learned.
## 
## .
## └── house
##     ├── smallstuff
##     │   ├── pencil.txt
##     │   ├── marker.txt
##     │   └── eraser.txt
##     └── furniture
##         ├── chair.txt
##         ├── table.txt
##         └── desk.txt
##
## Consider: After you create the directory structure and files show above (the 'tree'), from what 
## directory location can you run the 'tree' command to see the entire tree.
## Try this: Change to the home directory (cd ~).
## Using 'home' as your current directory, how can you modify and use the tree command to see the 
## same tree structure shown above (no more, no less)?   I.e., Run tree without using the cd command a second time.

## 31
## You can evaluate a command within another command:
echo "Right now the date and time is $(date)" >> myfile.txt 


## 32
## Try this. It displays the path of the "working directory", that is, the one where your terminal is focused.
pwd


## 33
## Use cd to change your directory back to /tmp/otherstuff .


## 34
## Use output redirection, that is, the > character, to write the current working directory to a file.


## 35
## Here's how to copy a file, and then display it using cat.
## Note that this will only work if you start by changing your directory (cd) to where pencil.txt is located.
cp pencil.txt writing_tool.txt
cat writing_tool.txt


## 36
## Here's how to remove a file. Be very careful, as it skips the trash can, and does not confirm before removing! 
## How to be careful: 
##  - Avoid wildcards (the * character) with rm
##  - Use cat to view the file before removing it
rm writing_tool.txt


## 37
## Try this. You can see that the grep command displays all occurences of the word "to".
## Don't forget the asterisk in the grep command. The asterisk means "everything in my current directory".
cd /tmp/otherstuff/house/smallstuff
echo "Makes it easier to focus your eyes." > eyeglasses.txt 
echo "A great place to hike." > mountains.txt 
grep to *


## 37b
## To move something, use mv:
cd /tmp/otherstuff/house
echo "A comfortable place to sit." > couch.txt
mv couch.txt furniture


## 37c
## You can also use the special two dots that we saw when we were using cd:
cd /tmp/otherstuff/house/smallstuff
ls
mv mountains.txt ..
ls
cd ..
ls


## 37d
## Make a directory called "scenery", and move mountains.txt into it.


## 38
## Make a few example text files for yourself. Be sure to include the word "explore" in some of the files.
## Then, use grep to find occurences of the word "explore" in these files.


## 39
## grep can also search within subdirectories using the -r flag.
## Try this:
cd /tmp/otherstuff/
grep -r explore *


## 40
## Use grep to search for the letter "a" in all files in all subdirectories in /tmp/otherstuff.


## 41
## Copy and modify the previous example so that it uses output redirection to write grep's output to a file.


## 42
## To look back on what commands you've used, you can run this:
history

```

At this point, if you finish before the rest of the class, or if you'd like more practice with the terminal, start working on one of these tutorials:

  - https://ubuntu.com/tutorials/command-line-for-beginners
  - https://linuxsurvival.com

Some misc shell concepts

```sh
mkdir cool
cd Desktop/cool
## touch with single word
## touch with space
## ls
## How to put an actual space
## now, remove everything one by one with rm
## Display something using cat
## Cat multiple
## Cat with output redirection
## Cat with *
## ls
## Grep multiple with explicitly listed file names
## Grep multiple with *
## cd
## touch
## pwd
```

</details>

