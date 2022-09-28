# Ex 2: Print and Input Statements
(This page: https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/ex_2_print_and_inputs.md)

Up to this point, we've been doing terminal commands, such as `ls` and `cd`. Now, we're going to start programming in Python.

We'll be primarily using Visual Studio Code (VS Code) as our editor for the Python code that we write. Here's how to get set-up:

- Open VS Code
- Open your folder using `File -> Open Folder`
- Create a file called `ex_2.py`
- Now that you have that file open, type this in that file:
     ```python3
     print("Here we go!")
     ```
- Press the "run" button. It's a triangle in the top-right corner. (If you do not see a "run" button, then maybe the Python extension is not installed in VS Code, or maybe the extension of your file name is not precisely '.py'.)
- It should display "Here we go!" at the bottom of the screen.
- If it ran successfully, then Comment (disable) that exercise using `Ctrl /` while your cursor is placed on that line of code, and try the next exercise.
- Ask if you have any questions.



<details><summary>

> __Note__ _(Click here to expand)_

</summary>

> ------
>  
> A great supplemental resource is https://learn.arcade.academy . They start talking about `print` on Chapter 4. Some notes before you head over to that site:
> 
> - It mentions "Installing the Python programming language". That's already done in our classroom.
> - It mentions "An integrated development environment (IDE) called PyCharm". We primarily use VSCode (not PyCharm) as our IDE.
> - It mentions a "Version control system" called git. Git is not required for this class, but interested readers are encouraged to explore it.
> - Sections 4.2 and 4.3 are PyCharm-specific. You can skip them.
>------

</details>

------

Before we get to the rest of the exercises, here's a little info about what we're doing. This quoted from https://learn.arcade.academy/en/latest/chapters/04_print_statement/print_statement.html .

> "In this chapter we’ll write our first programs using the most fundamental of all tools in the programmer’s toolbox, the **print** function. This function does exactly what you’d expect––it prints to the screen.  
>   
> "While a lot of programs are graphics-based, text-only programs are still quite common with people that manage computers, or who do data analytics. Even for the graphics-based games we develop in this book, the **print** function will be a vital aid in understanding and debugging our games."


## Exercises
### Using Simple Print Statements

```python3
## 1 
## Try this.
print("Here we go!")
     
## 2
## Try this.
## You'll get an error having to do with the quotation marks.
## Why do you think that is? How do you fix it?
print(“bob”)


## 2b
## Try this.
print("If you want \n separate lines, you \n can do it \n like this.")


## 2c
## Try this.
print("This thing inside quotes is called a \"string\". If you want to put quotes inside, this is how.")
```

### Using Variables

So now, you've displayed some text on the screen. We may also want to store data. To do that, you use a **variable**.

If you'd like to read more about variables, go to section 7.1 on this page: https://learn.arcade.academy/en/latest/chapters/07_expressions/expressions.html


```python3
## 3
## Try this.
## firstn and lastn are the two variables in this example.

firstn = "Bob"
lastn = "Smith"
print(firstn)
print(lastn)


## 4
## Try this.
## This example uses a formatted string, which is called an f string for short. 
firstn = "Bob"
lastn = "Smith"
print(f"My name is {firstn} {lastn}")
```

### Using Input Statements

Now that we've seen some basic examples, let's ask the user to give us some info.

Who is the user? Well, imagine that you write the code, run the program, and then hand the keyboard to your neighbor. Imagine that your neighbor sees this:

```
Hello!
Say the name of a car, then press enter: 
```

Hopefully, your neighbor (the user) will type a car name. Regardless of what he/she types, the computer will reply like so:

```
The car you named is ____. That was a good choice.
```

However, instead of a blank, it will show the name of the car that the user typed.

Try it out:

```python3
## 4b
## Try this. When you run it, it will ask you to type something.
print("Hello!")
cartype = input("Say the name of a car, then press enter: ")
print(f"The car you named is {cartype}. That was a good choice.")
```

Here's some practice:

```python3
## 4c
## Copy and modify the previous example so that it asks the user for the name of a car,
## and then prints "The car you named is ____. Do you have one?"
## In the blank, you should say the car that the user named.


## 4d
## Copy and modify the previous example so that it asks the user for the name of an animal,
## and then prints "The animal you named is ____. I think that it would make a nice pet."


## 5
## Try this.
firstn = input("What is your first name?")
lastn = "Smith"
print(f"Your name is {firstn} {lastn}.")


## 6
## Copy and modify the previous example to do the following:
##  - Ask the user for his/her first name.
##  - Ask the user for his/her last name.
##  - Print "Your name is ___  ___."

## 6b
## Ask the user for their first name, middle name, and last name.
## Print "Your name is __ __ __" (filling in their first name, middle name, and last name).


## 7
## Ask the user for a color, and then say
## "___ is a pretty color."
## (Fill in the blank with the actual color.)


## 8
## Ask the user for the name of an animal and a plant.
## Then display "The ___ eats ___ every day",
## but fill in the blanks with the animal and the plant.
```

### Using Strings and Integers

```python3
## 9
## Try this.
a = "Hello"
b = "Goodbye"
c = a + b
print(c)


## 10
## Try this.
a = input("First word? ")
b = input("Second word? ")
c = a + b
print(c)


## 11
## Try this.
a = 5
b = 3
c = a + b
print(c)


## 12
## Try this.
a = "5"
b = "3"
c = a + b
print(c)


## 13 
## Try this.
a = int("5")
b = int("3")
c = a + b
print(c)


## 14
## Try this.
a = input("Type an integer.")
b = input("Type another integer.")
c = a + b
print(c)


## 15
## Try this.
a = int(input("Type an integer."))
b = int(input("Type another integer."))
c = a + b
print(c)


## 16
## Try this. You will get an error. How do you fix it?
a = input("Type an integer.")
b = int(input("Type another integer."))
c = a + b
print(c)

## 17
## Try this. You will get an error. How do you fix it?
favnum = input("What is your favorite number?")
onemore = favnum + 1
print(f"One more would be {onemore}.")


## 18
## Ask the user for two integers.
## Display "The sum of your two numbers is ___".


## 19
## Ask the user for two integers.
## Display "The first number minus the second number is ___".


## 20
## Ask the user for an integer.
## Display "That number plus 2 is ___".


## 21
## Ask the user for a number.
## Display "Half of that number is ___".


## 22
## Ask the user for the number of questions on a test,
## and ask "how many did you get right?"
## Then, display "You got ___% right". (You'll need to calculate the percent.)


## 23
##### You may wonder why you must use the int() function.
##### After all, shouldn't the computer know what a number looks like?
##### Here's an example of when you WOULDN'T want the number to be treated as an integer.

########################################
# Right way:
beg = "800"
mid = "555"
end = input("Can you give me some random last four digits please? ")

fullPhoneNum = beg + mid + end
print(fullPhoneNum)


########################################
# Wrong way:
beg = 800
mid = 555
end = int(input("Can you give me some random last four digits please? "))

fullPhoneNum = beg + mid + end
print(fullPhoneNum)

########################################
# Another wrong way:
beg = 800
mid = 555
end = input("Can you give me some random last four digits please? ")

fullPhoneNum = beg + mid + end
print(fullPhoneNum)
```