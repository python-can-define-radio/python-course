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
print("You win the game if your age is exactly 99.")
age = input("How old are you? ")
if age == 99:
    print("You win!")
else:
    print("You lose.")

    
