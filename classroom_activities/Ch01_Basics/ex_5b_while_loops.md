# While Loops

The `while` loop is useful for situations in which you don't know how many repetitions will be needed. For example, if you make a word-guessing game, you don't know how many times the user will guess incorrectly, or how long the user will want to play. You also have no reason to continue prompting the user for guesses after the user has guessed correctly. The `while` loop allows you to loop "while the guess is not yet matching the secret word", or more generally, "while some condition is still being met".

You may wonder how to know whether to use a `for` loop or a `while` loop. Generally...

- A `for` loop is useful when you have a known collection to iterate through, such as a list of names.
- A `while` loop is useful when the loop will continue for an unknown number of iterations.

ℹ️ Use Ctrl + C to exit a program (useful for exiting infinite loops).

ℹ️ This material coincides with material from python slideshow C (slides 22-29).

### Exercises

```python3
## 1
## Try this.
count = 10
print(f"count is {count}.")
count += 1
print(f"I changed count. Now, it's {count}.")
count -= 2
print(f"I changed it again. Now, it's {count}.")


## 2
## Modify the above example so it asks the user for a number.


## 3
## Try this.
count = 3
print(count)
count -= 1
print(count)
count -= 1
print(count)
count -= 1
print("Reached zero. Proof:")
print(count)


## 4
## Let's make the previous example less repetitive.
## Try this:
count = 3
while count > 0:
    print(count)
    count -= 1
print("Reached zero. Proof:")
print(count)


## 5
## Modify the previous example to let the user pick where to start the count.


## 6
## Modify the previous example to display
## "Launch in 3"
## "Launch in 2"
## "Launch in 1"
## "Liftoff!"


## 7
## Try this:
import time
print("Start...")
time.sleep(1)
print("Done.")


## 8
## Modify the previous example to let the user pick the number of delay seconds.


## 9
## Modify the earlier "Liftoff" example to add a small delay to make it more fun.
## (It should wait a second after each number is displayed.)
```

Often in programming, [TIMTOWTDI](https://wiki.c2.com/?ThereIsMoreThanOneWayToDoIt) (There Is More Than One Way To Do It). In the context of `while` loops, you can choose to use the `break` statement to exit the loop before reaching the end of the current loop iteration. 

Many of the examples that follow will show both approaches.

```python3
## 10
## Try this.
keepGoing = "yes"
while keepGoing == "yes":
    print("Since the variable keepGoing is still 'yes', I am going to keep going.")
    keepGoing = input("Do you want me to keep going? ")
print("Ok, you typed something other than 'yes', so I stopped.")


## 11
## Copy and modify the previous example like so:
## If the user types "y", then keep looping.


## 12
## Try this:
keepGoing = "yes"
while keepGoing == "yes" or keepGoing == "y":
    print("Continuing.")
    keepGoing = input("Do you want me to keep going? ")
print("Ok, stopping.")


## 13
## Here's another way to do it:
keepGoing = "yes"
while keepGoing in ["yes", "y"]:
    print("Continuing.")
    keepGoing = input("Do you want me to keep going? ")
print("Ok, stopping.")


## 14
## Here's the opposite:
keepGoing = "yes"
while keepGoing not in ["no", "no thanks"]:
    print("Continuing.")
    keepGoing = input("Do you want me to keep going? ")
print("Ok, stopping.")   


## 14b
## This example is functionally equivalent, but uses the `break` approach.
## Notice that this avoids having to initialize a variable before the loop.
while 2 + 2 == 4:
    print("Continuing.")
    keepGoing = input("Do you want me to keep going? ")
    if keepGoing in ["no", "no thanks"]:
        break
print("Ok, stopping.")


## 15
## Copy one of the previous two examples. Change it like so:
## Continue looping if the user types any of these: "hey", "woo", or "yes".


## 16
## Copy and modify the previous example like so:
## If the user types anything other than "no", then keep going.
## (So the user could type "yes", "hi", etc.)
## Recommendation: you can use the != operator, which means "not equal",
##  or you can use `not in` as shown above.


## 17
## Copy and modify the previous example like so:
## Keep going if the user types anything other than these: "done", "quit", "exit".
## ALSO, make it case-insensitive (capitalization does not affect outcome).


## 18
## Create a program that keeps track of a count.
## Example run:
##  The counter is currently 0.
##  Would you like to add one, subtract one, or quit? add
##  The counter is currently 1.
##  Would you like to add one, subtract one, or quit? add
##  The counter is currently 2.
##  Would you like to add one, subtract one, or quit? subtract
##  The counter is currently 1.
##  Would you like to add one, subtract one, or quit? quit
##  Your final tally is 1.
##  Thanks for using my counter program!


## 19
## Try this.
print("Welcome to the word guesser!")
secretWord = "water"
guess = ""
while guess != secretWord:
    guess = input("What is your guess? ")
print("You got it!")


## 19b
## Again, this is functionally equivalent to the previous example, but uses break.
print("Welcome to the word guesser!")
secretWord = "water"
while 5 == 5:
    guess = input("What is your guess? ")
    if guess == secretWord:
        break
print("You got it!")


## 20
## Copy and modify one of the two previous examples so that each iteration
## of the loop displays "Let me check to determine whether that's right."


## 21
## Here's a variation that displays "No, try again" in each
## iteration of the loop, but only if the guess was wrong.
## Notice that to accomplish this, we must ask for input
## twice: before the loop and inside the loop.
print("Welcome to the word guesser!")
secretWord = "water"
guess = input("What is your guess? ")
while guess != secretWord:
    print("No, try again.")
    guess = input("What is your guess? ")
print("You got it!")


## 21b
## This is an example that shows the advantage of using `break`:
## it avoids having a duplicate input().
print("Welcome to the word guesser!")
secretWord = "water"
while 1 < 2:
    guess = input("What is your guess? ")
    if guess == secretWord:
        print("You got it!")
        break
    else:
        print("No, try again.")

## 22
## Try this.
## Note: we must set `num` to something before the loop starts,
##       so I arbitrarily picked 0.
print("Welcome to the number doubler.")
num = 0
while num != -1:
    num = int(input("Type a number, or type -1 to quit: "))
    print(f"Double your num is {num * 2}.")
print("Exiting.")


## 22b
## Try this. Again, using `break` avoids...
## - having to initialize a variable before the loop, and
## - duplicate inputs
print("Welcome to the number doubler.")
while True:
    num = int(input("Type a number, or type -1 to quit: "))
    if num == -1:
        print("Exiting.")
        break
    else:
        print(f"Double your num is {num * 2}.")


## 23
## Copy and modify one of the two previous examples so
## that instead of doubling numbers,
## it calculates the number squared.


## 24
## Copy and modify the previous example so that it does not display
## the doubled number if the user enters -1.


## 25
animal = input("Name an animal, or say 'moose' to exit: ")
while animal != "moose":
    print(f"The {animal} says 'meow'.")
    animal = input("Name an animal, or say 'moose' to exit: ")
print("Moose out.")


## 26
## Copy and modify the previous example so that
## it asks for both the name of the animal and what the animal says.
## Instead of "The ___ says 'meow'", display "The ___ says '___'."


## 27
## Copy and modify the previous example so that it only exits the loop
## if the animal is "moose" and the sound is "meow".
## Think about whether you should use `and` or `or` in this context.


## 28    
## Have you ever played the game Duck Duck Goose?
import random
import time

print("This is a Duck, Duck, Goose Simulator. Have fun!!!!!")
choices = ["Goose",
              "Duck",
              "Duck",
              "Duck"]
one_choice = random.choice(choices)
while one_choice != "Goose":
    print(f"{one_choice}...")
    one_choice = random.choice(choices)
    time.sleep(0.5)
print("Goose!")  


## 29
## Make a word guesser:
##  - When the program starts, display "Welcome to the word guesser!"
##  - Ask the user to guess the secret word.
##  - If the user guesses the word correctly, display "You got it!" and stop asking for guesses.
##  - If the user guesses incorrectly, then randomly display one of these replies:
##        "Not yet, try again."
##        "I bet you'll get it, keep trying!"
##        "That's not it."
##        "I appreciate your patience, but you haven't guessed it yet."
##  - The program must loop to allow the user to continue guessing until 
##    he/she correctly guesses the secret word.
##  - The program must allow the user to guess the word regardless of capitalization.
##      Recommendation: Refer back to the exercises that used .lower(), which
##                      you can find by using the multi-file search feature of
##                      VS Code. (Many other editors also have this feature.)


## 29b
## Make a program that asks the user for names.
## If the name starts with "c", append it to a list.
## At the end, display only the names that start with c.
## The structure will look like this:
##   names_starting_with_c = []
##   name = input("Enter a name, or q to quit: ")
##   while ???:
##       if ???:
##           names_starting_with_c.append(???)
##       name = input("Enter a name, or q to quit: ")
##   print(f"These names start with the letter c: {names_starting_with_c}")
## Example run:
##   Enter a name: bob
##   Enter a name: chris
##   Enter a name: corey
##   Enter a name: q
##   These names start with the letter c: ['chris', 'corey']


## 30
## Make a remainder study tool:
## Have Python pick a random number between 20 and 100.
## Ask the user: "If you divided {the_randomly_chosen_number} by 12, what would be the remainder?"
## Allow the user to guess repeatedly until the user correctly guesses the remainder.
## Example run:
## If you divided 27 by 12, what would be the remainder?
## Guess: 5
## Guess: 2
## Guess: 3
## You got it!
```

### Extra questions (If you've reached this point, feel free to move on to the next exercise set).

```python3
## 31
## {Do this exercise after you've learned to write files.}
## Display "This is a grade tracking helper."
## Open a file named "physics_grades.csv" for writing.
## Write to the file: "StudentName,StudentGrade"
## Ask the user: "What is the total number of questions for this assignment? "
## In a loop:
##    Ask the user: "What is the student name? (Press enter with no name to exit.) "
##    If the user entered nothing, then close the file, display "Exiting..." and exit the loop.
##    If the user entered a name:
##      Ask the user: "How many questions did that student answer correctly? "
##      Compute the percent score for that student.
##      Display the percent, rounded to 2 decimal places.
##      Write to the file: "Bob,92.36%" (but with the actual name and percent instead).
## NOTE: After you have tested your program, try opening the physics_grades.csv file
## in a spreadsheet program such as Libreoffice Calc.


## 32
## Try this.
## As a reminder, use Ctrl + C to exit a program (useful for exiting infinite loops).
x = 0
while 2 + 2 == 4:
    print(x)
    x += 1
print("Done")
## What happened?
    
    
## 33
## Try this.
while 2 + 2 == 5:
    print("Hi")
print("Done")


## 34
## Try this.
while 3 > 2:
    print("Hi")
print("Done")


## 35
## Try this.
while 2 == 2:
    print("Hi")
print("Done")


## 36
## Try this.
while True == True:
    print("Hi")
print("Done")


## 37
## Try this. It's a little less obvious.
while True:
    print("Hi")
print("Done")


## 38
## Try this.
while 1 == 1:
    color = input("What is your favorite color?")
    print(f"Ok, {color} is a nice color.")

    
## 39
## Try this.
print("Welcome to yet another version of the number doubler.")
while True:
    num = int(input("Type a number, or type -1 to quit: "))
    if num == -1:
        break
    print(f"Double your num is {num * 2}.")
    
```
