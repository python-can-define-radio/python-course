```python3

"""Excercises 6a while-loops
"""

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


## 12a
## Here's another way to do it:
keepGoing = "yes"
while keepGoing in ["yes", "y"]:
    print("Continuing.")
    keepGoing = input("Do you want me to keep going? ")
print("Ok, stopping.")


## 12b
## Here's the opposite:
keepGoing = "yes"
while keepGoing not in ["no", "no thanks"]:
    print("Continuing.")
    keepGoing = input("Do you want me to keep going? ")
print("Ok, stopping.")   


## 13
## Copy and modify the previous example like so:
## Continue looping if the user types any of these: "hey", "woo", or "yes".


## 14
## Copy and modify the previous example like so:
## If the user types anything other than "no", then keep going.
## (So the user could type "yes", "hi", etc.)
## Reminder: The != operator means "not equal".


## 14b
## Copy and modify the previous example like so:
## Keep going if the user types anything other than these: "done", "quit", "exit".
## ALSO, make it case-insensitive (capitalization does not affect outcome).


## 14c
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


## 15
## Try this.
print("Welcome to the word guesser!")
guess = ""
secretWord = "water"
while guess != secretWord:
    guess = input("What is your guess? ")
print("You got it!")


## 16
## Copy and modify the previous example so that each iteration
## of the loop displays "Let me check to determine whether that's right."


## 17
## Copy and modify the previous example so that each 
## iteration of the loop displays "No, try again"
## (but only if the guess was wrong).


## 18
## Try this.
## Note: we must set `num` to something before the loop starts,
##       so I arbitrarily picked 0.
print("Welcome to the number doubler.")
num = 0
while num != -1:
    num = int(input("Type a number, or type -1 to quit: "))
    print(f"Double your num is {num * 2}.")


## 19
## Copy and modify the previous example so that instead of doubling numbers,
## it calculates the number squared.


## 20
## Copy and modify the previous example so that it does not display
## the doubled number if the user enters -1.


## 21
## Try this.
## As a reminder, use Ctrl + C to exit a program.
x = 0
while 2 + 2 == 4:
    print(x)
    x += 1
print("Done")
    
    
## 22
## Try this.
while 2 + 2 == 5:
    print("Hi")
print("Done")


## 23
## Try this.
while 3 > 2:
    print("Hi")
print("Done")


## 24
## Try this.
while 2 == 2:
    print("Hi")
print("Done")


## 25
## Try this.
while True == True:
    print("Hi")
print("Done")


## 26
## Try this. It's a little less obvious.
while True:
    print("Hi")
print("Done")


## 27
## Make a loop that displays a message of your choice
## repeatedly forever.


## 28
## Try this.
while 1 == 1:
    color = input("What is your favorite color?")
    print(f"Ok, {color} is a nice color.")


## 29
## Copy and modify the previous example so that in
## every iteration of the loop, it asks the user for the name of an animal,
## and then it displays "The ____ says 'meow'."


## 30
## Copy and modify the previous example so that
## it asks for both the name of the animal and what the animal says,
## and then displays "The ___ says '___'."


## 31
## Copy and modify the previous example so that
## if the animal is "cat" and the sound is "meow",
## it exits the loop.
## The command for exiting the loop is `break`.
## An example of how to use `break` is below.


## 31b:
## Try this. Feel free to customize it for fun.
peoplelist = ["Charlie",
              "Bob",
              "Jake",
              "Bilee",
              "Hanner",
              "Jaqura"]
while 1 == 1:
    person = random.choice(peoplelist)
    print(person)
    if person == "Jake" or person == "Bilee":
        print("Woo!")
        break
    time.sleep(0.5)


## 32
## Try this.
print("Welcome to another version of the number doubler.")
while True:
    num = int(input("Type a number, or type -1 to quit: "))
    if num == -1:
        break
    print(f"Double your num is {num * 2}.")


## 33
## Make a word guesser:
##  - When the program starts, display "Welcome to the word guesser!"
##  - Ask the user to guess the secret word.
##  - If the user guesses the word correctly, display "You got it!" and exit the loop.
##  - If the user guesses incorrectly, then randomly display one of these replies:
##        "Not yet, try again."
##        "I bet you'll get it, keep trying!"
##        "That's not it."
##        "I appreciate your patience, but you haven't guessed it yet."
##  - The program must loop to allow the user to continue guessing until he/she correctly guesses the secret word.
##  - The program must allow the user to guess the word regardless of capitalization.
##      Recommended: refer back to the exercise that used .lower() .


## 34
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


## 35
## (challenge question)
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
## NOTE: After you have tested your program, try opening the physics_grades.csv file in a spreadsheet program such as Libreoffice Calc.
```
](https://meet.jit.si/ynbgybggtyhfrthderfdrtyhgyu






```python3

"""Excercises 6a while-loops
"""

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


## 15
## Copy and modify the previous example like so:
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


## 20
## Copy and modify the previous example so that each iteration
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


## 23
## Copy and modify the previous example so that instead of doubling numbers,
## it calculates the number squared.


## 24
## Copy and modify the previous example so that it does not display
## the doubled number if the user enters -1.
## Hint: Try this structure:
##   - Before the loop, ask the user for input, and save it in `num`.
##   - Re-order the commands within the loop.


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
##      Recommended: refer back to the exercise that used .lower() .


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


## 31
## (challenge question)
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
## NOTE: After you have tested your program, try opening the physics_grades.csv file in a spreadsheet program such as Libreoffice Calc.

```

## Extra questions

### If you've reached this point, feel free to move on to the next exercise set.

```python3
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


)https://meet.jit.si/ynbgybggtyhfrthderfdrtyhgyu






```python3

"""Excercises 6a while-loops
"""

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


## 15
## Copy and modify the previous example like so:
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


## 20
## Copy and modify the previous example so that each iteration
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


## 23
## Copy and modify the previous example so that instead of doubling numbers,
## it calculates the number squared.


## 24
## Copy and modify the previous example so that it does not display
## the doubled number if the user enters -1.
## Hint: Try this structure:
##   - Before the loop, ask the user for input, and save it in `num`.
##   - Re-order the commands within the loop.


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
##      Recommended: refer back to the exercise that used .lower() .


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


## 31
## (challenge question)
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
## NOTE: After you have tested your program, try opening the physics_grades.csv file in a spreadsheet program such as Libreoffice Calc.

```

## Extra questions

### If you've reached this point, feel free to move on to the next exercise set.

```python3
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


