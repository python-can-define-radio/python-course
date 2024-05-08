
# Functions

Functions are an essential building block in almost any programming language. They help to organize code into pieces of functionality, which reduces complexity. They also reduce the length of your code by allowing for code to be reused throughout your program without copy/pasting.

ℹ️ This material coincides with material from python slideshow C (slides 30-38).

### Exercises

### A very simple function

Let's start with some basic functions. These first examples will feel contrived; the usefulness will become clearer later in this lesson.

```python3
## 1
## Try this.
def sayWelcome():
    print("Welcome to the Python class")
    print("We hope you enjoy it.")
    print()

sayWelcome()
sayWelcome()
```

The first line, `def sayWelcome()`, means "Define a function named `sayWelcome()`. The next three `print` lines are called the "body" of the function. Just as with `if`, `while`, and `for` statements, you must indent the body of the function so that Python knows what is inside the function and what is not.

The last two lines are simply `sayWelcome()`. Those are the lines that _call_ (or _run_) the function. Let's experiment:

```python3
## 2
## Try this. How many times does it display the welcome text?
def sayWelcome():
    print("Welcome to the Python class")
    print("We hope you enjoy it.")
    print()

sayWelcome()
sayWelcome()
sayWelcome()


## 3
## Try this. How many times does it display the welcome text?
def sayWelcome():
    print("Welcome to the Python class")
    print("We hope you enjoy it.")
    print()
```

Notice in the previous example that simply defining a function does not run it. If you want the function to run, you must _call_ it.

Let's explore the impact of this.

```python3
## 4
## Try this. Does it display in the order that you expect?
def sayWelcome():
    print("Welcome to the Python class")
    print("We hope you enjoy it.")
    print()

def sayBye():
    print("Goodbye, have a good day!")

sayBye()
sayWelcome()


## 5
## Copy and modify the previous example to make
## it call sayWelcome before it calls sayBye.


## 6
## Try this. Why doesn't it work?
## How could you define a function so that this will run?
sayCoolStuff()
```

For the sake of keeping code organized, functions should usually be defined at the beginning of your code, just after any `import` statements you may have. For example:

```python3
## 7
## This is an example showing where to position function definitions.
def sayWelcome():
    print("Welcome to the Python class")
    print("We hope you enjoy it.")
    print()

print("This line of code is not well positioned -- it comes between two function definitions.")

def sayBye():
    print("Goodbye, have a good day!")

print("This line of code is well positioned, because it comes after the function definitions.")
```

### Function parameters

There are many cases in which it's helpful to reuse a piece of code with only small changes. **Parameters** help accomplish this.

```python3
## 8a
## Try this.
def sayHiTo(name):
    print(f"Hello {name}. Welcome to the Python course.")

sayHiTo("Bob")
sayHiTo("Sue")
sayHiTo("Tom")
```

Notice that we never write `name = "Bob"` -- there are no `=` signs anywhere! What is Python doing?

When we write `def sayHiTo(name)`, the `name` is a **parameter**. Parameters tell Python how to use the **arguments** that are given when we call the function.

You can have multiple parameters:

```python3
## 8b
## Try this.
def tellAbout(name, animal):
    print(f"Hello {name}. I've heard you have a pet {animal}.")

tellAbout("Bob", "cat")
tellAbout("Sue", "dog")
tellAbout("camel", "Tom")


## 9
## Copy and modify the previous example so that
## Tom has a pet camel, rather than vice versa.
```

Another important aspect: if you don't give the right number of arguments when you call the function, you'll get an error message:

```python3
## 10
## Try this. It will give an error message.
def tellAbout(name, animal):
    print(f"Hello {name}. I've heard you have a pet {animal}.")

tellAbout("Bob")


## 11
## Copy and modify the previous example so that Bob has a pet animal.
```

Up to this point, our arguments have been literal strings, such as `"Bob"`, `"dog"`, etc. The argument can also be a variable:

```python3
## 12
## Try this.
def tellAbout(name, animal):
    print(f"Hello {name}. I've heard you have a pet {animal}.")

na = "Bob"
ani = "cat"
tellAbout(na, ani)
```

Notice that the variables that are used as arguments do not have to match the function parameters. 

```python3
## 13
## Copy and modify the previous example so that `na` and `ani` are set by user input.
```

Now that we have parameters at our disposal, we can make some more interesting functions:

```python3
## 14
## Try this.
def sayLengthOfEach(names):
    for name in names:
        print(f"The length of {name} is {len(name)}")

sayLengthOfEach(["Bob", "Joseph", "Susan"])
```

### The `return` statement

We've shown how to put data into a function using parameters. Here's how to get the data back out of the function:

```python3
## 15
## Try this.
def convertHoursToMinutes(hours):
    return hours * 60

h = int(input("Give a number of hours, and I'll convert it to minutes."))
m = convertHoursToMinutes(h)
print(f"That would be {m} minutes.")
```

### Writing test cases

Another very useful feature of functions is the ability to make testable pieces of code.

Using the `convertHoursToMinutes` example:

```python3
## 16
## Try this.
print(convertHoursToMinutes(2))
```

Given that we know that 2 hours is 120 minutes, we expect the above example to print `120`.

We can actually state that in our code using an `assert` statement. Here's an example of an incorrect assertion:

```python3
## 17
## Try this.
assert convertHoursToMinutes(2) == 119
```

When you run that, it should say `AssertionError`. (If it shows anything else, ask an instructor.)

To fix that test, we would write `assert convertHoursToMinutes(2) == 120`. If you fix it, you'll notice that it produces no output. That's to be expected.

### Practice

```python3
## 18
## Define a function that converts from feet to yards.
## Use this structure:
def convertFeetToYards(feet):
    return _____

print(convertFeetToYards(5))


## 19
## Write two `assert` statements to check that convertFeetToYards is working correctly.
```
