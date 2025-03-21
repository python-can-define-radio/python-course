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


## 5 Try this.
## This gives us a list of 50 integers.
x = list(range(50))    ## Note: on 2025 March 20 we changed this to `list(range(50))`.
print(x)
## What does this give us? Try running it multiple times with different values for `k`.
print(random.sample(x, 5))


## 6
## Make a list of five numbers.  Print "I randomly picked a number, and I got ____".


## 7
## Copy and modify the previous example.
## After displaying the number you picked,
## if the randomly picked number was more than 40, print "It was a big number."
## Otherwise, print "It was not a very big number."


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
