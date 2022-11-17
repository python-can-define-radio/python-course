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
## Copy and modify the previous example like so:
## Continue looping if the user types any of these: "hey", "woo", or "yes".
## Note: I recommend trying the two exercises in the file ex_3b_if_else_common_condition_mistake.py
##       to avoid a common subtle mistake.


## 14
## Copy and modify the previous example like so:
## If the user types anything other than "no", then keep going.
## (So the user could type "yes", "hi", etc.)


## 15
## Try this.
## Reminder: the != operator means "Not equal".
print("Welcome to the word guesser!")
guess = ""
secretWord = "water"
while guess != secretWord:
    guess = input("What is your guess? ")
print("You got it!")


## 16
## Copy and modify the previous example so that each iteration
## of the loop displays "Let me check if that's right."


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
while 2 + 2 == 4:
    print("Hi")
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


## 25
## Try this. It's a little less obvious.
while True:
    print("Hi")
print("Done")


## 26
## Make a loop that displays a message of your choice
## repeatedly forever.


## 27
## Try this.
while 1 == 1:
    color = input("What is your favorite color?")
    print(f"Ok, {color} is a nice color.")


## 25
## Copy and modify the previous example so that in
## every iteration of the loop, it asks the user for the name of an animal,
## and then it displays "The ____ says 'meow'."


## 26
## Copy and modify the previous example so that
## it asks for both the name of the animal and what the animal says,
## and then displays "The ___ says '___'."


## 27
## Copy and modify the previous example so that
## if the animal is "cat" and the sound is "meow",
## it exits the loop.
## The command for exiting the loop is `break`.
## An example of how to use `break` is below.


## 28
## Try this.
print("Welcome to another version of the number doubler.")
while True:
    num = int(input("Type a number, or type -1 to quit: "))
    if num == -1:
        break
    print(f"Double your num is {num * 2}.")


## 29
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


## 30
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
