# Randomness

### Exercises
Using Python's random module -- Making random selections from lists & Generating random numbers

```python3

## Before starting the exercise, type this at the top of your file:
import random


## Once you've added that, try these exercises.

## 1
## Try this.
things = ["dinosaur", "dog", "cat"]
print(random.choice(things))


## 2
## Make a list of five words of your choice. Print a randomly chosen word.


## 3
## Make a list of five phrases (instead of single words). Print a randomly chosen phrase.


## 4
## Try this.
nums = [28, 99, 7]
oneNum = random.choice(nums)
print(oneNum)


## 4b  (Note: Renumbered on 2025 July 21)
## Copy and modify the previous example.
## After displaying the number you picked,
## if the randomly picked number was more than 40, print "It was a big number."
## Otherwise, print "It was not a very big number."



## 5 Try this.
## This gives us a list of 10 integers.
x = list(range(10))
## which is the same as this (you can use either one)
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   
print(x)
## What does this give us? Try running it multiple times with different values for `k`.
print(random.sample(x, 5))


## 6
## Make a list of at least five numbers.  
## using random.sample(), select at least two numbers from the list.
## Display "I randomly picked these numbers, and I got ____".


## 7
## (Note: this was edited on 2025 July 21)
## Make a list of at least five strings.
## Using random.sample, do the same as you did in the previous exercise.


## 8
## Try this.
## Does the randomly chosen number include the endpoint?
## (In other words, is it similar to range?)
num = random.randint(3, 6)
print(num)


## 9
## Make a random score generator using randint.
## Give the user a randomly chosen score: display "You got a ___ on the test".
## (It's up to you how high or low you want your random grades to be.)


## 10 Random Floating Point Number
## Try this.
x = random.random()  #Generates a random floating point number from 0.0 to 1.0
print(x)


## 11 Random Floating Point Number, modified
## What does this do?  (I.e., What are the possible values of y?)
x = random.random()
y = x + 3
print(f"{y:0.5f}")


## 12 Random Floating Point Number of an Arbitrary Size.
## (optional challenge question)
## Using the previous example (i.e., x = random.random() ), instead of addition,
## what operation could you perform so y is a random number between zero and 
## a chosen maximum value?
## For example, how could you generate numbers between 0 and 5, or 0 and 100?
## Prove your theory in Python.
```

```python3
## 13
## Try this. Run it more than once.
import random
randomNumber = random.randint(5, 8)
print(f"Here is a random integer: {randomNumber}")


## 14
## Copy and modify the above example so that the computer will 
## pick numbers between 1 and 4 instead.


## 15
## Try this. Run it a few times.
import random
randomNumber = random.randint(5, 8)
print(f"Here is a random integer: {randomNumber}")
if randomNumber == 7:
    print("I think some people say that number is lucky.")


## 16
## Copy and modify the previous example so that the computer
## will pick numbers between 7 and 10 instead.


## 17
## Copy and modify the previous example so that if the randomly
## chosen number is 10, it will say "Wow, a two digit number!"
```

```python3
## 18
## Try this.
import random
name = random.choice(["bob", "susan", "joe", "anna"])
print(f"Hey {name}.") 
if name == "joe":
    print("Your name rhymes with low.") 
     

## 19
## Copy and modify the above example so that "dell" is one of the names
## that can be randomly chosen.


## 20
## Copy and modify the above example so that 
## if the name is "dell", it will print "That’s a computer brand."


## 21
## Try this.
## Notice that the "Have a good day" line prints regardless of
## the chosen name.  This is because it is
## not indented (it has no spaces before the line).
import random
name = random.choice(["bob", "susan", "joe", "anna"])
print(f"Hey {name}.") 
if name == "joe":
    print("Hello Joe!")
    print("Your name rhymes with low.")
print("Have a good day.")


## 22
## Try this.
import random
age = random.randint(18, 24)
print(f"Pretend that you are {age} years old.")
if age < 21: 
    print("You can't drink alcohol in the US yet.") 
else: 
    print("You are legally allowed to drink. Drink responsibly 😊 ") 
     

## 23
## Copy and modify the above example so that the
## legal drinking age is 40. (Just to be funny.) 
```
