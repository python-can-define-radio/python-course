# If-Else Common Mistakes

At this point, you've seen multiple examples of correct ways to use `input` and `if`. Now, we'll explore some common mistakes.

ℹ️ This material coincides with material from python slideshow C (slides 39-46).

### Exercises

Let's start with a simple example:

```python3
## prac1
name1 = "Bob"
name2 = "Joe"
if name1 == name2:
    print("Something happened.")
```

What would happen if we changed it to this?

```python3
## prac1b
name1 = "Bob"
if name1:
    print("Something happened.")
```

What does `if name1` mean? It turns out that that's equivalent to this:

```python3
## prac1c
name1 = "Bob"
if name1 != "":
    print("Something happened.")
```

What if you're working with a number?

```python3
## prac1d
somenumber = 2
if somenumber:
    print("Something happened.")
```

That's equivalent to this:

```python3
## prac1e
somenumber = 2
if somenumber != 0:
    print("Something happened.")
```

Given these somewhat confusing behaviors, we generally recommend that beginner-level students avoid this way of using an if statement. Ask if this is unclear.

```python3
## 1
## Try this.
guess = input("Guess one of my words: ")
if guess == "water" or guess == "food":
    print("You were right.")
else:
    print("Sorry, not right.")


## 2
## Try this. Test it thoroughly.
## (DON'T DO THIS IN REAL CODE. You'll see why.)
guess = input("Guess one of my words: ")
if guess == "water" or "food":
    print("You were right.")
else:
    print("Sorry, not right.")

## 3
## Ask an instructor if you are unclear about the purpose
## of those two exercises.

#############################################################

## 4
## What's wrong with this code?
input("What is your name? ")
if "Bob":
    print("Hello Robert.")

    
## 5
## What's wrong with this code?
name = input("What is your name? ")
if "Bob":
    print("Hello Robert.")
    

## 6
## What's wrong with this code?
input("What is your name? ")
if input == "Bob":
    print("Hello Robert.")

    
## 7 
## What's wrong with this code?
name = print(input("What is your name? "))
if name == "Bob":
    print("Hello Robert.")
    
    
## 8
## What's wrong with this code?
name = input(print("What is your name? "))
if name == "Bob":
    print("Hello Robert.")


## 8b
## This isn't wrong, but it is certainly confusing.
## You shouldn't do this in real code.
## However, it may help you understand what's wrong with the next few examples.
name = input("What is your name? ")
George = "Bob"
if name == George:
    print("This will print if they typed Bob.")
else:
    print("This will print for any other name, including the one that starts with a G and ends with eorge.")


## 9
## What's wrong with this code?
first = int(input("Give me a number. "))
operation = input("Do you want to double the number or half it? Say either 'double' or 'half'.")
double = first * 2
half = first / 2
if double:
    print(f"Ok, double your number is {double}.")
if half:
    print(f"Ok, half your number is {half}.")
    
    
## 10
## What's wrong with this code?
first = int(input("Give me a number. "))
operation = input("Do you want to double the number or half it? Say either 'double' or 'half'.")
double = first * 2
half = first / 2
if operation == double:
    print(f"Ok, double your number is {double}.")
if operation == half:
    print(f"Ok, half your number is {half}.")


## 11
## What's wrong with this code?
print("You win the game if your age is at least 90.")
age = input("How old are you? ")
if age >= 90:
    print("You win!")
else:
    print("You lose.")


## 11b
## What's wrong with this code?
print("You win the game if your age is exactly 99.")
age = input("How old are you? ")
if age == 99:
    print("You win!")
else:
    print("You lose.")


## 12
## What's wrong with this code?
opinion = input("Do you like celery? ")
if opinion == "yes" and opinion == "definitely":
    print("Glad you like it.")
else:
    print("You don't like it? You should try it again some time.")


## 13
## What's wrong with this code? The fix is to change the `or` to `and`, but why?
response = input("There are two correct words you can guess. ")
if response != "marker" or response != "board":
    print("Not correct. Try again.")
else:
    print("You guessed it!")
    

## 13b
## What's wrong with this code?
name = input("What is your name? ")
if name.lower == "bob":
    print("Hey Bobby!")
else:
    print("Hello, good to meet you.")


## 13c
## What's wrong with this code?
name = input("What is your name? ")
if name.lower() == "Bob":
    print("Hey Bobby!")
else:
    print("Hello, good to meet you.")


## 14
## What's wrong with this code?
## For reference, see the "What color is water" examples in ex_3a_if_else. 
opinion = input("Do you like celery? ")
like = ["yes", "Yes", "YES"]
if like:
    print("Glad you like it.")
else:
    print("You don't like it? You should try it again some time.")


## 15
## What's wrong with this code?
opinion = input("Do you like celery? ")
like = ["yes", "Yes", "YES"]
if opinion == like:
    print("Glad you like it.")
else:
    print("You don't like it? You should try it again some time.")


## 16
## What's wrong with this code?
opinion = input("Do you like celery? ")
if opinion == ["yes", "Yes", "YES"]:
    print("Glad you like it.")
else:
    print("You don't like it? You should try it again some time.")

```
