# Print and Input Statements

Up to this point, we've been doing terminal commands, such as `ls` and `cd`. Now, we're going to start programming in Python.

We'll be primarily using Visual Studio Code (VS Code) as our editor for the Python code that we write. Another editor option is called Thonny. However, its primary use for the purposes of this class will be debugging.
<details><summary>Here's how to get set-up for VS Code:</summary>

- Open VS Code
- Open your folder using `File -> Open Folder` (If needed, first create a folder using the Terminal or the file managment program.)
- Create a file called `ex_2a_print_inputs.py`
- Now that you have that file open, type this in that file:
     ```python3
     print("Here we go!")
     ```
- Save the file to your local drive by press the key combination {Ctrl}{S} or by using the "File/Save" menu command.
- Open the VS Code terminal by pressing `View -> Terminal`, or using the keyboard shortcut <code>Ctrl `</code>.
- Type `python3 ex_2a_print_inputs.py` and press enter.
- It should display "Here we go!" in the terminal.
- Ask if you have any questions.
</details>
<details><summary>Here's how to get set-up for Thonny:</summary>

- Open a terminal window and type `source ~/.profile` and hit enter. (This allows you to launch thonny without (a)logging-out & logging-in again OR (b) rebooting the computer. ...Although, those are valid options.)
- Type `thonny` and hit enter.
- Once Thonny opens, click `View > Files` to see the complete file structure.
    - You may also want to select Variables and/or Assistant to open their panes as well.
- Navigate to your personal folder in the Files pane on the left.
- Create a file called `ex_2a_print_inputs.py`
- Now that you have that file open, type this in that file:
     ```python3
     print("Here we go!")
     ```
- Save the file to your local drive by press the key combination {Ctrl}{S} or by using the "File>Save" menu command.
- Press F5 or the Play ▶️ at the top left of your screen to run the script.
- It should display "Here we go!" in the terminal.
- Ask if you have any questions.
</details>

ℹ️ This material coincides with material from python slideshow B (slides 1-11, 16, 69). 

### Background info

Before we get to the rest of the exercises, here's a little info about what we're doing. This quoted from https://learn.arcade.academy/en/latest/chapters/04_print_statement/print_statement.html .

> "In this chapter we’ll write our first programs using the most fundamental of all tools in the programmer’s toolbox, the **print** function. This function does exactly what you’d expect––it prints to the screen.  
>   
> "While a lot of programs are graphics-based, text-only programs are still quite common with people that manage computers, or who do data analytics. Even for the graphics-based games we develop in this book, the **print** function will be a vital aid in understanding and debugging our games."


### Exercises

#### Using Simple Print Statements

```python3
## 1 
## Try this.
print("Here we go!")

## 1b
## Try this.
print("I can print")
print("more than one line.")
```

Once you have run both of those exercises, you can "comment out the lines", that is, disable them. Here's how:

- In the editor, place your cursor on any part of the line (for example, the "n" of `print`).
- Press `Ctrl` + `/` in VS Code, or `Ctrl` + `3` in Thonny. You'll see that the line is now preceded by a "#", and turns a different color. This indicates that it is "Commented" (disabled), that is, it will no longer run.

Example:
```python3
# print("This line won't run because it is 'commented out'. ")
# print("Any line preceded by a '#' will not run.")
```

We speak of commenting frequently, so here are some example sentences to show how the phrase is used:

- "Comment out those lines"
- "Disable those lines"
- "Those lines are commented out"
- "Comment them out"
- "Rem those out" (_The verb "rem" comes from "remark", which is a synonym for comment._)
- "Rem them out"

You can manually add the `#` characters if you want, but we recommend using the aforementioned keyboard shortcuts (`Ctrl` + `/` in VS Code, or `Ctrl` + `3` in Thonny).

Commenting out the exercises as you go is a great idea because it allows you to keep them for reference, but not see the output every time you press run.

Speaking of comments, you'll see that we've numbered our exercises. Number them accordingly on your computer as you work through them, as it makes them easier to find later. Also, we (the instructors) may refer to a specific exercise by number.

```python3
## 2a
## Try this.
print("If you want \n separate lines, you \n can also do it \n like this.")


## 2b
## Try this.
print("This thing inside quotes is called a \"string\". If you want")
print("to put quotes inside of quotes, you precede the quotes with a backslash.")
```

The backslash (`\`) is the character that always begins an 'escape sequence' in Python. An escape sequence can have one of two uses:
- It allows you type special characters, such as newline (`\n`).
- It allows you to type characters in a string that would normally have special meaning in Python, such as `"`.

```python3
## 2c
## Try this.
print("""If you put three quote marks, 
you can easily enter a
multi-line
string.""")


## 2d
## You can also use triple quotes similarly to how you use comments:
"""If I wanted to write a long explanation,
I could write it like this
instead of using the '#' if I wanted to."""


## 2e
## Try this.
print('In Python, the single quote can be used instead of the double quote.')
print("You can put 'single quotes' inside of double quotes, or vice versa, without needing an escape sequence.")
print('However, if you want single quotes inside of single quotes, you\'ll need to escape them using a backslash.')
```

#### Using Variables

At this point, you've displayed some text on the screen. We may also want to store data, and give it a specific name. In programming, this storage is done using a **variable**.

If you'd like to read more about variables, go to section 7.1 on this page: https://learn.arcade.academy/en/latest/chapters/07_expressions/expressions.html

```python3
## 3a
## Try this.
## firstn and lastn are the two variables in this example.
## When you run this, you won't see Smith. Why not?

firstn = "Bob"
lastn = "Smith"
print(firstn)


## 3b
## Copy and modify the previous example so that it
## prints firstn, and then prints lastn.


## 4a
## Try this.
## This example uses an f-string. The f stands for "format".
## f-strings are used to insert variables inside of a string.
firstn = "Bob"
lastn = "Smith"
print(f"My name is {firstn} {lastn}")


## 4b
## You can also use commas, but only in functions that
## support it, such as print.
## (Later, when we get to file writing, the 
## comma approach doesn't work, but f-strings do work.)
print("My name is", firstn, lastn)

## (Remember to define your variables.  Where should the variable definitions be placed to be effective?)
```

#### Using the Debugger

The debugger is useful for watching your code as it runs. Thonny's debugger is particularly useful, as it evaluates individual steps within a line of code.

To debug in Thonny, press `Ctrl` + `F5`.

To debug in VS Code, place a breakpoint (a red dot; ask an instructor to demonstrate) on a the line of code on which you'd like to begin debugging (the first line if you aren't sure), and then press `F5`.

For more information on debugging in Thonny, see the [Thonny homepage](https://thonny.org/), or ask an instructor.

For a short video on debugging with Thonny go [here](https://www.youtube.com/watch?v=QQAqQp06nXo).

#### Using Input Statements

Now that we've seen some basic examples, let's ask the user to give us some info.

Who is the user? Well, imagine that you write the code, run the program, and then hand the keyboard to your neighbor. Imagine that your neighbor sees this:

```
Hello!
Type the name of a car, then press enter: 
```

Hopefully, your neighbor (the user) will type a car name. Regardless of what he/she types, the computer will reply like so:

```
The car you named is ____. That was a good choice.
```

However, instead of a blank, it will show the name of the car that the user typed.

Try it out:

```python3
## 4c
## Try this.
## When you run it, it will ask you to type something.
## You will need to click inside the terminal on the bottom half of the screen
##   so that it has "focus" (that is, you want the words you type
##   to be entered in the terminal).
print("Hello!")
cartype = input("Type the name of a car, then press enter: ")
print(f"The car you named is {cartype}. That was a good choice.")
```

Here's some practice:

```python3
## 4d
## Copy and modify the previous example so that it asks the user for the name of a car,
## and then prints "The car you named is ____. Do you have one?"
## In the blank, you should include whatever car the user named.


## 4e
## Copy and modify the previous example so that it asks the user for the name of an animal,
## and then prints "The animal you named is ____. I think that it would make a nice pet."
########################
##  INSTRUCTOR-CHECK  ##
########################
## (Questions marked as INSTRUCTOR-CHECK are ones for which you should
##  show your answer to an instructor to verify that it fulfills the intent of the question.)


## 5
## Try this.
firstn = input("Please enter a first name? ")
lastn = "Smith"
print(f"Maybe someone is named: {firstn} {lastn}.")


## 6a
## Copy and modify the previous example to do the following:
##  - Ask the user for his/her first name.
##  - Ask the user for his/her last name.
##  - Print "Your name is ___  ___."


## 6b
## Ask the user for their first name, middle name, and last name.
## Print "Your name is __ __ __" (filling in their first name,
##                                 middle name, and last name).


## 7
## Ask the user for a color, and then say
## "___ is a pretty color."
## (Fill in the blank with the color that the user said.)


## 8
## Ask the user for the name of an animal and of a plant.
## Then display "The ___ eats ___ every day",
## but fill in the blanks with the animal and the plant the user entered.
```

#### Using Strings and Integers

The word "string" simply means a sequence of characters. "Bob" is a string; "I am at the store" is a string.

Programming languages treat numbers differently from strings. For example, we all know that `2 + 3` is `5`. But what is `"Hello" + "Goodbye"`? 

```python3
## 9a
## Try this.
a = "Hello"
b = "Goodbye"
c = a + b
print(c)


## 9b
mysentence = "Hello" + "everyone"
print(mysentence)


## 9c
## Copy and modify the previous example so that 
## it displays a space: "Hello everyone" rather than "Helloeveryone".
```

As you can see, `a + b` was `"HelloGoodbye"`. The fancy name to say "add strings" is _concatenate_, which simply means putting the two strings next to each other, as shown above.

You can also let the user enter the words to be concatenated.

```python3
## 10
## Try this.
a = input("First word? ")
b = input("Second word? ")
c = a + b
print(c)
```

Now, how does the computer know whether you want to do math addition or string concatenation?

Try these:

```python3
## 11
a = 5
b = 3
c = a + b
print(c)


## 12
a = "5"
b = "3"
c = a + b
print(c)
```

As you can see, if you add two strings (the things insides quotation marks), it will concatenate: `"5" + "3"` is `"53"`.

On the other hand, if you add two integers, it will do math addition: `5 + 3` is `8`.

Let's look at why that matters when working with inputs.

```python3
## 13 
print("Welcome to the number adder that doesn't work right!")
a = input("What's a number you like? ")
b = input("Can you give me another number you like? ")
c = a + b
print("I added them. Here's what I got...")
print(c)
```

Try some easy numbers to check it. Does it do the right thing?

Now, compare to this one:

```python3
## 14
## Try this.  It will perform proper arithmetic.
print("Welcome to the number adder that works well!")
a = int(input("What's a number you like? "))
b = int(input("Can you give me another number you like? "))
c = a + b
print(c)
```

Notice that the `int` function tells Python to convert the numbers to integers. If you use `input` without `int`, then the variables are strings (not integers), so the `+` symbol does concatenation instead of math addition.

```python3
## 15
## Try this. You will get an error. How do you fix it?
a = input("What is a number you like? ")
b = int(input("Can you give me another number you like? "))
c = a + b
print(c)


## 16
## Try this. You will get an error. How do you fix it?
favnum = input("What is your favorite number? ")
onemore = favnum + 1
print(f"One more would be {onemore}")


## 17
## Ask the user for an integer.
## Display "That number plus 2 is ___".
########################
##  INSTRUCTOR-CHECK  ##
########################


## 18
## Ask the user for two integers.
## Display "The sum of your two numbers is ___".


## 19
## Ask the user for two integers.
## Display "The first number minus the second number is ___".


## 20
## Ask the user for a number.
## Display "Half of that number is ___".


## 21a
## Try this.
print("Hello"*3)


## 21b
## Copy and modify the previous example to ask the user for a string.
## Display whatever string the user enters three times 
##  (using *3, as in the previous example).


## 22a
## Try this. It will give an error.
print("Hello" * "3")


## 22b
## Copy and modify the previous example to ask the user for both the
## string to be multiplied and the number of repetitions.
## Hint: If you get an error, is it the same error as in the `print("Hello" * "3")` example? If so, why?


## 23
## Does this example do what you expect?
## Why does it repeat the number five times rather than doing "real" math multiplication?
## How do you make it do math?
num = input("Give me a number. ")
print("I'm going to try to multiply that number by 5,")
print("but something strange is going to happen:")
print(num*5)


## 24
## Ask the user for the number of questions on a test,
## and ask "how many did you get right?"
## Then, display "You got ___% right". (You'll need to calculate the percent.)
########################
##  INSTRUCTOR-CHECK  ##
########################


## 25
## Ask the user for name and age.
## Display "Guess what, ___, in two years you'll be ___."
## (The user-provided name goes in the first blank, and the
##   age two years from now in the second blank.)


## 26
## Try this.
## Notice: The type of `x` is integer, and the type of `y` is string.
## The type of 3 is integer.
## What happens when you multiply and integer times an integer?
## What about a string times an integer?
x = 123
y = "123"
print(x*3)
print(y*3)


## 27
## Try this. It shows how to use the type() function.
## `x` and `y` are both variables, are they integers or strings?
x = input("Enter a word.")
y = int(input("Enter a number."))
print(f"The type of x is {type(x)}, which is another way to say 'string'.")
print(f"The type of y is {type(y)}, which is another way to say 'integer'.")
print(x*y)



## 28a
## Determine the type of each of these variables (integer, string, or something else).
## Hint: Python can tell you the types using the type() function.
mystery = 6
another = "Hello"
something = input("Enter a number.")
whatIsThis = int(input("Enter a number."))
thisIsSomething = 3.1
```

In the previous question, you discovered that the type of `thisIsSomething` was "float", not "integer".

The "float" type (which means floating point, referring to the decimal point) is able to hold numbers that are not whole numbers.

```python3
## Try this. It will give an error. If it doesn't, please ask an instructor.
## 28b
somenum = int(input("Try typing a non-whole number, such as an approximate value for pi. You'll see that it doesn't work: "))
print(f"You typed {somenum}")


## 28c
## Try this. You'll see that it allows for non-whole numbers.
somenum = float(input("Try typing another non-whole number: "))
print(f"You typed {somenum}")


## 28d
## Ask the user for two numbers.
## Use float() in the places where you would use int().
## Display "The sum of your two numbers is ___".


## 28e
## Ask the user for a number, making sure that you allow for non-whole numbers.
## Display "Twice that number is ___".
## Example run:
##    Can you give me a number? 3.4
##    Twice that number is 6.8
```

You may wonder -- why not always use `float()`? There are at least two reasons:

1. There are cases in which you don't want to allow for non-whole values. For example, `numberOfPeople = float(input("How many people attended the event? "))` would not make much sense!
2. Math with integers is faster than math with floats. This is significant, for example, when you're processing millions of data points every second (such as when doing real-time signal processing).
3. There are certain cases in which you must use an int; for example, `print("Hello"*3.5)` will give an error.

```python3
## 28f
## For extra practice with floats, copy and modify some of your previous exercises
##   so they use float instead of int.


## 29
## Try this. You will get an error. Why?
## (Note: This isn't fixable. It's a purely educational question.)
x = "hello"
y = "goodbye"
print(x*y)


## 30
## Try this. You will get an error. Why?
## (Note: no need to try to fix this. It's a purely educational question.)
x = "3"
y = "5"
print(x*y)
```

### Optional exercises

You may wonder why you must use the int() function. After all, shouldn't the computer know what a number looks like?

Here's an example of when you WOULDN'T want the number to be an integer. (In other words, you want the number to be a string.)

```python3
## 31a
# This is the right way:
beg = "800"
mid = "555"
end = input("Give me a 4 digit number: ")

print("Here's an example phone number using the digits you gave me:")
fullPhoneNum = beg + mid + end
print(fullPhoneNum)


# 31b
# The following version runs, but the output is wrong.
# What's wrong with the output?
beg = 800
mid = 555
end = int(input("Give me a 4 digit number: "))

print("Here's an example phone number using the digits you gave me:")
fullPhoneNum = beg + mid + end
print(fullPhoneNum)


# 31c
# Another wrong way:
# Why does this fail to run? 
# Changing the input(...) to int(input(...)) is NOT the solution. Why not?
beg = 800
mid = 555
end = input("Give me a 4 digit number: ")

print("Here's an example phone number using the digits you gave me:")
fullPhoneNum = beg + mid + end
print(fullPhoneNum)
```

<details><summary>Notes:</summary>

- If you press <kbd>Shift Enter</kbd>, you can cause issues. Ask the instructor to demonstrate (it's difficult to explain textually).
- The instructor will demonstrate how to use VS Code's multi-file search.
  
</details>

<details><summary> :information_source: For more information on Prints and Inputs <i>(Click here to expand)</i></summary>

> ```
> A great supplemental resource is https://learn.arcade.academy .
> They start talking about `print` on Chapter 4.
> Some notes before you head over to that site:
>  
> - It mentions "Installing the Python programming language". That's already done in our classroom.
> - It mentions "An integrated development environment (IDE) called PyCharm". We 
>      primarily use VSCode (not PyCharm) as our IDE.
> - It mentions a "Version control system" called git. Git is not required for
>      this class, but interested readers are encouraged to explore it.
> - Sections 4.2 and 4.3 are PyCharm-specific. You can skip them.
> ```
</details>

(This page: https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch01_Basics/ex_2a_print_and_inputs.md)
