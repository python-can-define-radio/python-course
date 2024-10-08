# Print and Input Statements

Up to this point, we've been doing terminal commands, such as `ls` and `cd`. Now, we're going to start programming in Python.

We'll be primarily using Visual Studio Code (VS Code) as our editor for the Python code that we write. Another editor option is called Thonny. However, its primary use for the purposes of this class will be debugging.
<details><summary>Here's how to get set-up for VS Code:</summary>

- Open VS Code
- Open your folder using `File -> Open Folder` (If needed, first create a folder using the Terminal or the file managment program.)
- Create a file called `ex_1a_print_and_inputs.py`
- Now that you have that file open, type this in that file:
     ```python3
     print("Here we go!")
     ```
- Save the file to your local drive by press the key combination {Ctrl}{S} or by using the "File/Save" menu command.
- Open the VS Code terminal by pressing `View -> Terminal`, or using the keyboard shortcut <code>Ctrl `</code>.
- Type `python3 ex_1a_print_and_inputs.py` and press enter.
- It should display "Here we go!" in the terminal.
- Ask if you have any questions.
</details>
<details><summary>Here's how to get set-up for Thonny:</summary>

- Open a terminal window and type `source ~/.profile` and hit enter. (This allows you to launch thonny without (a)logging-out & logging-in again OR (b) rebooting the computer. ...Although, those are valid options.)
- In the terminal window type `thonny` and hit enter.
- Once Thonny opens, click `View > Files` to see the complete file structure.
    - You may also want to select Variables and/or Assistant to open their panes as well.
- Navigate to your personal folder in the Files pane on the left.
- Create a file called `ex_1a_print_and_inputs.py`
- Now that you have that file open, type this in that file:
     ```python3
     print("Here we go!")
     ```
- Save the file to your local drive by press the key combination {Ctrl}{S} or by using the "File>Save" menu command.
- Press F5 or the Play ▶️ at the top left of your screen to run the script.
- It should display "Here we go!" in the terminal.
- Ask if you have any questions.
</details>
<details><summary>Here's how to get set-up for BlockPy:</summary>
     
- Go to https://think.cs.vt.edu/blockpy/
- In the row that says `Blocks | Split | Text`, click "Split".
- Either drag blocks or write code.
- Press Run.
</details>

ℹ️ This material coincides with material from python slideshow B (slides 1-11, 16, 24, 54-63, 69). 

### Exercises

#### Variables

Let's start by creating some **variables**. Variables are used to store data, and give it a specific name.

```python3
## 1
number_of_magic_beans = 5
price_per_bean = 3
tot_price = number_of_magic_beans * price_per_bean
print("The total price:")
print(tot_price)
```

In this example, we created three variables:

- `number_of_magic_beans`, which contains the integer 5.
- `price_per_bean`, which contains the integer 3.
- `tot_price`, which contains the integer 15.

_Understanding check:_ What is an integer?

- We use the `print` function twice:
  - The line `print("The total price:")` displays the text `The total price:` on the screen.
  - The line `print(tot_price)` displays the contents of `tot_price`, that is, `15`.

Notice the difference: the first `print`, which uses quotation marks, displays the literal text. The second `print`, which does not use quotation marks, treats `tot_price` as a variable.

```python3
## 2
## Complete this code so that it calculates and displays the total number of fruits.
apples = 3
bananas = 5
fruit_total = ___ + ___
print("Total number of fruits:")
print(___)

## 3
## Complete this code so that it calculates and displays the speed.
distance = 50
time = 5
speed = ___ / ___
print("The speed is...")
print(___)

## 4
## Write an example that uses subtraction. Show an instructor.
```

At this point, it's useful to "comment out the lines", that is, disable them. Here's how:

- In the editor, place your cursor on any part of the line (for example, the "n" of `print`).
- Press `Ctrl` + `/` in VS Code, or `Ctrl` + `3` in Thonny. You'll see that the line is now preceded by a "#", and turns a different color. This indicates that it is "Commented" (disabled), that is, it will no longer run.
  - Note: If you're using BlockPy, we recommend that you copy the exercises to either Thonny or VS Code.

You can manually add the `#` characters if you want, but we recommend using the aforementioned keyboard shortcuts (`Ctrl` + `/` in VS Code, or `Ctrl` + `3` in Thonny).

Commenting out the exercises as you go is a great idea because it allows you to keep them for reference, but not see the output every time you press run.

Speaking of comments, you'll see that we've numbered our exercises. Number them accordingly on your computer as you work through them, as it makes them easier to find later. Also, we (the instructors) may refer to a specific exercise by number.

### ***ℹ️ To save yourself from unecessary work, do not delete the exercises when you complete them.*** 
### ***Comment them out and keep them for reference.***  
### ***These are your notes and can be used on the exam.***
### ***If you are unsure what the recommended workflow should be, ask an instructor to demonstrate. ℹ️***

#### Strings

We've seen that you can store integers in variables, for example, `apples = 3`.

You can also store **strings** (text) in variables:

```python3
## 5
greeting = "Hello"
customer = "Bob"
combined = greeting + customer
print(combined)
```

Notice that the `+` acts differently for strings than it does for integers. Integers are added using math (that is, `5 + 3` becomes `8`), but strings are placed next to each other (`"Hello"` + `"Bob"` becomes `"HelloBob"`). This is called "concatenation", which means "to chain together".

Here are some other examples of what we can do with strings:

```python3
## 6
greeting = "hello"
customer = "bob"
combined = greeting + " " + customer
shouted = combined.upper()
print(shouted)
no_cap = combined.lower()
print(no_cap)
full_sentence = combined + ".... Are you learning python today?"
capi = full_sentence.capitalize()
print(capi)
```

Now, try it by filling in the blanks:

```python3
## 7
## Complete the following:
customer = "caTHy"
shouted_cust = ___.upper()
print("The customer name, all uppercase, is...")
print(shouted_cust)
print("The customer name, all lowercase, is...")
print(___.lower())
print("The customer name, with proper capitalization, is...")
print(customer.___())
```

You can also check the length of a string:

```python3
## 8
a_long_word = "antidisestablishmentarianism"
print("The length of the long word is")
print(len(a_long_word))
print("The length of the word 'hi' is ")
print(len('hi'))
```

### Using variables inline

When we use `print`, the thing that is being printed is called an "argument".

Examples:

- In `print(5)`, the argument is `5`.
- In `print("hello")`, the argument is `"hello"`.

You can also use `print` with multiple arguments:

```python3
## 9
apples = 3
print("I have", apples, "apples.")
```

Notice that when `"apples"` is in quotes, it's treated as a string (the literal word "apples"), while `apples` outside of quotes is interpreted as a variable.

You can also use a **formatted string**, a.k.a. **f-string**:

```python3
## 10
apples = 3
print(f"I have {apples} apples.")
```

### Common error messages so far

Here are some troubleshooting techniques for errors you might have encountered.

Example 1:

```python3
## 11
## Try this. You will get an error message.
apples = 3
print(appls)
```

This will show the following error message:

```
Traceback (most recent call last):
  ...
NameError: name 'appls' is not defined
```

Python is trying to say the following: "You asked me to display the contents of a variable called `appls`, but there aren't any variables called `appls`.

In that case, the solution is fairly clear -- fix the spelling.

Example 2:

```python3
## 11
## Try this. You will get an error message.
print(hello)
```

This will show the following error message:

```
Traceback (most recent call last):
  ...
NameError: name 'hello' is not defined
```

The error is the same as before, but the reason is different: in this case, we're trying to display the literal text "hello", but Python doesn't know that -- it assumes that hello refers to a variable, and there is no variable called "hello" in this program. The solution: tell Python that we want to display the _string_ "hello": `print("hello")`.

### Inputs

You can make programs interactive by using the `input()` function. Here's an example:

```python3
## 11
print("Enter the customer name: ")
customer = input()
greeting = "hello " + customer + "!"
print(greeting.upper())
```

When you run this, you'll see that the `input` function causes the program to pause. The `input()` means "Wait for the user to type something before moving on."

Who is "the user"? Well, imagine that you write the code, run the program, and then hand the keyboard to your neighbor. In this case, your neighbor is the "user". You should act as though the user can't see the Python code -- he/she can only see the output of the program as it is running. 

Practice:

```python3
## 11
## Fill in the blanks.
print("Enter a color: ")
color = input()
print("Enter an animal: ")
___ = input()
print("Enter a plant: ")
plant = ___()
print("The color you chose is", color)
print("The animal you chose is", ___)
print("The plant you chose is", plant)


## 12
## Fill in the blanks.
print("Enter the name of a car.")
___ = input()
print("The car you named is", somecar)
length_carname = len(___)
print("That car's name contains", length_carname, "characters.")


## 13
## Ask the user to enter the name of a planet.
## Display "That planet in all capital letters would be ___".


## 13
## Ask the user to enter the name of a planet.
## Display "That planet's name is ___ characters long".
#####################
## INSTRUCTOR CHECK
#####################
## (Questions marked as INSTRUCTOR-CHECK are ones for which you should
##  show your answer to an instructor to verify that it fulfills the intent of the question.)


## 14
## Ask the user for the name of an animal,
## and then print "The animal you named is ____. I think that it would make a nice pet."
## Example run:
##   Type the name of an animal: ✎ dog
##   The animal you named is dog. I think that it would make a nice pet.
## (The "✎" emoji is optional. It indicates where the user
##  will enter input.)


## 15
## Ask the user for the name of an animal and of a plant.
## Then display "The ___ eats ___ every day",
## but fill in the blanks with the animal and the plant the user entered.
```

#### More about data types

We've seen two data types so far: strings and integers. We've also seen that the way `+` works depends on the data type. Here's a brief review:

```python3
## 16
apples = 3
print("I have", apples, "apples.")
onemore = apples + 1
print("If I had another, I would have", onemore, "apples.")
planet = "Mars"
print("Here's a planet name:", planet)
followed = planet + "1"
print("Here's that planet's name, followed by the number 1:", followed)
```

What happens if we try to mix types?
```python3
## 17
## Try this. You will see an error.
planet = "Mars"
apples = 3
print(planet + apples)
```

Running this will display...

```
Traceback (most recent call last):
  ...
TypeError: can only concatenate str (not "int") to str
```

This is Python's way to say that...

TODO




```python3
## 2a
## Try this.
print("""If you put three quote marks, 
you can easily enter a
multi-line
string.""")


## 2e
## Try this.
print('In Python, the single quote can be used instead of the double quote.')
print('''You can use three single quotes
to make a multi-line string.''')
```

#### Using the Debugger

The debugger is useful for watching your code as it runs. Thonny's debugger is particularly useful, as it evaluates individual steps within a line of code.

To debug in Thonny, press `Ctrl` + `F5`.

To debug in VS Code, place a breakpoint (a red dot; ask an instructor to demonstrate) on a the line of code on which you'd like to begin debugging (the first line if you aren't sure), and then press `F5`.

For more information on debugging in Thonny, see the [Thonny homepage](https://thonny.org/), or ask an instructor.

For a short video on debugging with Thonny go [here](https://www.youtube.com/watch?v=QQAqQp06nXo).





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
```

### Notice:  Data "types"
Variables can hold any of several types of data,
e.g., integer, floating-point number, string, list, etc.
As we shall see later, Python includes a "type()" command to
determine what kind of data is held in a variable or a value.  
*For more information, See [../../resources/data_types.md](https://github.com/python-can-define-radio/python-course/blob/main/resources/data_types.md)*

```python3
## 26 Duplicating/repeating a string
## Try this.
## In the current example, the data type of `x` is integer, and the type of `y` is string.
## The type of 3 is integer.
## What happens when you multiply an integer times an integer?
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

The next exercise shows a common mistake.

```python3
## 30b
## What is wrong with this code?
a = int(input("First num?"))
b = int(input("Second num? "))
c = {a} + {b}
print(f"The sum is {c}.")
```

### Optional exercises

<details><summary>Expand here for additional content.</summary>
     
You may wonder why you must use the int() function. After all, shouldn't the computer know what a number looks like?

Here's an example of when you WOULDN'T want the number to be an integer. (In other words, you want the number to be a string.)

```python3
## 31a
## This is the right way:
beg = "800"
mid = "555"
end = input("Give me a 4 digit number: ")

print("Here's an example phone number using the digits you gave me:")
fullPhoneNum = beg + mid + end
print(fullPhoneNum)


## 31b
## The following version runs, but the output is wrong.
## What's wrong with the output?
beg = 800
mid = 555
end = int(input("Give me a 4 digit number: "))

print("Here's an example phone number using the digits you gave me:")
fullPhoneNum = beg + mid + end
print(fullPhoneNum)


## 31c
## Another wrong way:
## Why does this fail to run? 
## Changing the input(...) to int(input(...)) is NOT the solution. Why not?
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
</details>
