# Dictionaries

Dictionaries are a somewhat more advanced (but very useful) data structure.

These exercises show the basics. For more practice, see https://realpython.com/python-dicts/

ℹ️ This material coincides with material from python slideshow C (slides 14-21).

### Exercises

```python3
## 1
## Try this.
print("If you want to put everything", end="")
print("on one line, then you can", end="")
print("use this.")


## 2
## Try this.
mypersondata = {
  "firstname": "Bob",
  "lastname": "Smith",
  "age": 23
}
print(mypersondata["firstname"])


## 3
## Copy and modify the previous example so that it displays the last name instead of the first name.


## 4
## Try this.
mypersondata = {
  "firstname": "Bob",
  "lastname": "Smith",
  "age": 23
}
print(f'Do you know {mypersondata["firstname"]} ...?')
# NOTE: on previous line, we must use different types of quotation marks for the f-string vs. the dictionary address.


## 5
## Copy and modify the previous example so that it displays this:
##   'Did you know that ___   ___ is ___ years old?'
##   (Fill in the first name, last name, and age appropriately.)


## 6
## Try this.
namelocation = {
  "Sophia": "Greece",
  "Mario": "Italy",
  "Jaques": "France"
}

for name in namelocation:
    print(name)
    print("is from")
    print(namelocation[name])
    print()
    

## 7
## Try this.
namelocation = {
  "Sophia": "Greece",
  "Mario": "Italy",
  "Jaques": "France"
}

print("These people are from Greece:")
for name in namelocation:
    if namelocation[name] == "Greece":
        print(name)
    
## Alternate approach:
for name, loc in namelocation.items():
    if loc == "Greece":
        print(name)
```

### Example dictionary in use

```python3
import random
user = input("rock paper or scissors? ")

beats = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

choices = ["rock", "paper", "scissors"]
 
cpu = random.choice(choices)
print(f"cpu has selected: {cpu}")

if user == cpu:
    print("Tie")
elif beats[user] == cpu:
    print("You win!")
else:
    print("You lose!")
```
