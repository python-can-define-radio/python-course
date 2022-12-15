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
    
