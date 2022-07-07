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
## Note: I recommend trying the two exercises in the file ex_common_condition_mistake.py
##       to avoid a common subtle mistake.


## 14
## Copy and modify the previous example like so:
## If the user types anything other than "no", then keep going.


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

