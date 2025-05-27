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

## Exercises

### Variables

Let's start by creating some **variables**. Variables are used to store data.

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

_Definition:_ **Integer**:  
A whole number which may be positive, negative, or zero.

- We use the `print` function twice:
  - The line `print("The total price:")` displays the text `The total price:` on the screen.
  - The line `print(tot_price)` displays the contents of `tot_price`, that is, `15`.

Notice the difference: the first `print`, which uses quotation marks, displays the literal text. The second `print`, which does not use quotation marks, treats `tot_price` as a variable.

Let's discuss an error message you may come across at this point.

```python3
## 2
## Try this. It will produce an error.
number of magic beans = 5
```

What's different? This code attempts to create a variable, `number of magic beans`. However, variable names cannot have spaces, so when you try to run this, Python will produce a SyntaxError because it doesn't know how to read your code:

```
    number of magic beans = 5
           ^^
SyntaxError: invalid syntax
```

The word "syntax" means the arrangement of characters, words, and symbols. For example, "I food eat" is invalid English syntax because the verb, "eat", comes after the direct object, "food".

To learn more about variable name rules, see [here](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/variable_names.md).

```python3
## 3
## Complete this so that it calculates and displays the total number of fruits.
apples = 3
bananas = 5
fruit_total = ___ + ___
print("Total number of fruits:")
print(___)


## 4
## Complete this code so that it calculates and displays the speed.
distance = 50
time = 5
speed = ___ / ___
print("The speed is...")
print(___)


## 5
## Write an example that uses subtraction.
```

At this point, it's useful to "comment out the lines", that is, disable them. Here's how:

- In the editor, place your cursor on any part of the line (for example, the "n" of `print`).
- Press `Ctrl` + `/` in VS Code, or `Ctrl` + `3` in Thonny. You'll see that the line is now preceded by a "#", and turns a different color. This indicates that it is "Commented" (disabled), that is, it will no longer run.
  - Note: If you're using BlockPy, we recommend that you copy the exercises to either Thonny or VS Code.

You can manually add the `#` characters if you want, but we recommend using the aforementioned keyboard shortcuts (`Ctrl` + `/` in VS Code, or `Ctrl` + `3` in Thonny).

Commenting out the exercises as you go is a great idea because it allows you to keep them for reference, but not see the output every time you press run.

Speaking of comments, you'll see that we've numbered our exercises. Number them accordingly on your computer as you work through them, as it makes them easier to find later. Also, we (the instructors) may refer to a specific exercise by number.

***ℹ️ To save yourself from unecessary work, do not delete the exercises when you complete them.***  
***Comment them out and keep them for reference. These are your notes and can be used on the exam.***  
***If you are unsure what the recommended workflow should be, ask an instructor to demonstrate. ℹ️***

### Strings

We've seen that you can store integers in variables, for example, `apples = 3`.

You can also store **strings** in variables.

_Definition:_ **String**:  
Text. More precisely, a sequence of zero or more characters (letters, numbers, symbols, etc). Examples: `"Hi"`, `"bob is 3 years old"`, `":-)"`

```python3
## 6
greeting = "Hello"
customer = "Bob"
combined = greeting + customer
print(combined)
```

Notice that the `+` acts differently for strings than it does for integers. Integers are added using math (that is, `5 + 3` becomes `8`), but strings are placed next to each other (`"Hello"` + `"Bob"` becomes `"HelloBob"`). This is called "concatenation", which means "to chain together".

Here are some other examples of what we can do with strings:

```python3
## 7
## Try this. What is it doing?
shopper = "bob"
shouted = shopper.upper()
print(shouted)


## 8
## Try this. What is it doing?
greeted_shop = "HelLO BOb"
no_cap = greeted_shop.lower()
print(no_cap)


## 9
## Try this. What is it doing?
greet = "HelLOoOooOO"
capi = greet.capitalize()
print(capi)
```

Now, try it by filling in the blanks:

```python3
## 10
## Complete the following:
merchant = "caTHy"
print("The merchant name, all uppercase, is...")
print(merchant.___())
print("The merchant name, all lowercase, is...")
print(___.lower())
print("The merchant name, with proper capitalization, is...")
print(___.___())

########################
##  INSTRUCTOR-CHECK  ##
########################
## (Questions marked as INSTRUCTOR-CHECK are ones for which you should
##  show your answer to an instructor to verify that it fulfills the intent of the question.)
```


You can also check the length of a string:

```python3
## 11
a_long_word = "antidisestablishmentarianism"
print("The length of the long word is")
print(len(a_long_word))
print("The length of the word 'hi' is ")
print(len('hi'))
```

### Printing on multiple lines

There are numerous methods of printing on multiple lines available. These are some of the simplest:

- Use multiple print functions (print has a newline built-in by default).
     - `print("Hello World")`
     - `print("Welcome to")`
     - `print("the Python Course")`
- Use a Multi-line string (triple quotes).
     - <pre>print("""Hello World
        Welcome to 
        the Python Course""")</pre>
- Use the "\n" escape sequence inside your print function.
     - `print("Hello World\nWelcome to\nthe Python Course")`
     
### Using variables inline

When we use `print`, the thing that is being printed is called an "argument".

Examples:

- In `print(5)`, the argument is `5`.
- In `print("hello")`, the argument is `"hello"`.

You can also use `print` with multiple arguments:

```python3
## 12
grapes = 3
print("I have", grapes, "grapes.")
```

Notice that when `"grapes"` is in quotes, it's treated as a string (the literal word "grapes"), while `grapes` outside of quotes is interpreted as a variable.

You can also use a **formatted string**, a.k.a. **f-string**:

```python3
## 13
kiwis = 3
print(f"I have {kiwis} kiwis.")
```

### Common error messages so far

Here are some troubleshooting techniques for errors you might have encountered.

Example 1:

```python3
## 14
## Try this. You will get an error message.
melons = 3
print(melns)
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
## 15
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
## 16
print("Enter the customer name: ")
buyer = input()
salutation = "hello" + buyer + "!"
print(salutation.upper())
```

When you run this, you'll see that the `input` function causes the program to pause. The `input()` means "Wait for the user to type something before moving on."

Who is "the user"? Well, imagine that you write the code, run the program, and then hand the keyboard to your neighbor. In this case, your neighbor is the "user". You should act as though the user can't see the Python code -- he/she can only see the output of the program as it is running. 

Practice:

```python3
## 17
## Fill in the blanks.
print("Enter a color: ")
color = input()
print("Enter an animal: ")
___ = input()
print("Enter a plant: ")
plant = ___()
print("The color you chose is", ___)
print("The animal you chose is", animal)
print(___, plant)


## 18
## Fill in the blanks.
print("Enter the name of a car.")
___ = input()
print("The car you named is", somecar)
length_carname = len(___)
print("That car's name contains", length_carname, "characters.")


## 19
## Ask the user to enter the name of a planet.
## Display "That planet in all capital letters would be ___".


## 20
## Ask the user to enter the name of a planet.
## Display "That planet's name is ___ characters long".

######################
## INSTRUCTOR CHECK ##
######################


## 21
## Ask the user for the name of an animal,
## and then print "The animal you named is ____. I think that it would make a nice pet."
## Example run:
##   Type the name of an animal: ✎ dog
##   The animal you named is dog. I think that it would make a nice pet.
## (The "✎" emoji is optional. It indicates where the user
##  will enter input.)


## 22
## Ask the user for the name of an animal and of a plant.
## Then display "The ___ eats ___ every day",
## but fill in the blanks with the animal and the plant the user entered.
```

You can also combine the `print` and the `input` like so, if you prefer:

```python3
## 23
## Try this.
shade = input("Enter a color: ")
print("The color you chose is", shade)
```

Most of our examples use the combined approach, but either is valid.

### Data types

We've seen two data types so far: strings and integers. We've also seen that the way `+` works depends on the data type. Here's a brief review:

```python3
## 24
pears = 3
print("I have", pears, "pears.")
onemore = pears + 1
print("If I had another, I would have", onemore, "pears.")
planet = "Mars"
print("Here's a planet name:", planet)
followed = planet + "1"
print("Here's that planet's name, followed by the number 1:", followed)
```

What happens if we try to mix types?
```python3
## 25
## Try this. You will see an error.
space = "Mars"
plums = 3
print(space + plums)
```

Running this will display...

```
Traceback (most recent call last):
  ...
TypeError: can only concatenate str (not "int") to str
```

Here's what Python is saying:
- There's a `+`, so that means you're trying to add.
- The first one was a string, so that means the `+` is going to mean "concatenation" (not math adding).
- Concatenation only makes sense between strings, and `plums` is not a string. It's the integer 3.

Let's look at why that matters when working with inputs.

```python3
## 26 
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
## 27
## Try this.  It will perform proper arithmetic.
print("Welcome to the number adder that works well!")
a = int(input("What's a number you like? "))
b = int(input("Can you give me another number you like? "))
c = a + b
print(c)
```

Notice that the `int` function tells Python to convert the numbers to integers. If you use `input` without `int`, then the variables are strings (not integers), so the `+` symbol does concatenation instead of math addition.

```python3
## 28
## Try this. You will get an error. How do you fix it?
a = input("What is a number you like? ")
b = int(input("Can you give me another number you like? "))
c = a + b
print(c)


## 29
## Try this. You will get an error. How do you fix it?
favnum = input("What is your favorite number? ")
onemore = favnum + 1
print("One more would be", onemore)


## 30
## Ask the user for an integer.
## Display "That number plus 2 is ___".

########################
##  INSTRUCTOR-CHECK  ##
########################


## 32
## Ask the user for two integers.
## Display "The first number minus the second number is ___".


## 33
## Ask the user for a number.
## Display "Half of that number is ___".


## 34
## Try this.
print("Hello"*3)


## 35
## Copy and modify the previous example to ask the user for a string.
## Display whatever string the user enters three times 
##  (using *3, as in the previous example).


## 38
## Does this example do what you expect?
## Why does it repeat the number five times rather than doing "real" math multiplication?
## How do you make it do math?
num = input("Give me a number. ")
print("I'm going to try to multiply that number by 5,")
print("but something strange is going to happen:")
print(num*5)


## 39
## Ask the user for name and age.
## Display "Guess what, ___, in two years you'll be ___."
## (The user-provided name goes in the first blank, and the
##   age two years from now in the second blank.)


## 40
## Ask the user for the number of questions on a test,
## and ask "how many did you get right?"
## Then, display "You got ___% right". (You'll need to calculate the percent.)

########################
##  INSTRUCTOR-CHECK  ##
########################
```


### Notice:  Data "types"

Variables can hold any of several types of data,  
e.g., integer, floating-point number, string, list, etc.     
*For more information, See [../../resources/data_types.md](https://github.com/python-can-define-radio/python-course/blob/main/resources/data_types.md)*

```python3
## 41 Duplicating/repeating a string
## Try this.
## In the current example, the data type of `x` is integer, and the type of `y` is string.
## The type of 3 is integer.
## What happens when you multiply an integer times an integer?
## What about a string times an integer?
x = 123
y = "123"
print(x*3)
print(y*3)
```

The "float" type (which means floating point, referring to the decimal point) is able to hold numbers that are not whole numbers.

In VSCode it is relatively easy to find out the type of any variable or object just by using the mouseover hint,  
if you move your cursor over a variable you should see a smaller popup window which includes the type of that variable.

![mouseovervariable.png](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/mouseovervariable.png?raw=true)  

In the above image we see when I moved the mouse over the `name` variable the popup is saying `(variable) name: str` which means that the variable `name` is of the type string.  
Try mousing over variables in the next few examples to find out their type.

```python3
## Try this. It will give an error. If it doesn't, please ask an instructor.
## 44
somenum = int(input("Try typing a non-whole number, such as an approximate value for pi. You'll see that it doesn't work: "))
print(f"You typed {somenum}")


## 45
## Try this. You'll see that it allows for non-whole numbers.
somenum = float(input("Try typing another non-whole number: "))
print(f"You typed {somenum}")


## 46
## Ask the user for two numbers.
## Use float() in the places where you would use int().
## Display "The sum of your two numbers is ___".


## 47
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

For extra practice with floats, copy and modify some of your previous exercises so they use float instead of int.

The next exercise shows a common mistake.

```python3
## 49
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
## 50
## This is the right way:
beg = "800"
mid = "555"
end = input("Give me a 4 digit number: ")

print("Here's an example phone number using the digits you gave me:")
fullPhoneNum = beg + mid + end
print(fullPhoneNum)


## 51
## The following version runs, but the output is wrong.
## What's wrong with the output?
beg = 800
mid = 555
end = int(input("Give me a 4 digit number: "))

print("Here's an example phone number using the digits you gave me:")
fullPhoneNum = beg + mid + end
print(fullPhoneNum)


## 52
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

> A great supplemental resource is https://learn.arcade.academy  
> They start talking about `print` on Chapter 4.  
> Some notes before you head over to that site:
>  
> - It mentions "Installing the Python programming language". That's already done in our classroom.
> - It mentions "An integrated development environment (IDE) called PyCharm". We 
>      primarily use VSCode (not PyCharm) as our IDE.
> - It mentions a "Version control system" called git. Git is not required for
>      this class, but interested readers are encouraged to explore it.
> - Sections 4.2 and 4.3 are PyCharm-specific. You can skip them.

</details>
</details>
