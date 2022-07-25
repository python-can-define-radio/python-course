# 1
# Try this.


## 2
## Try this.
name = "bob"
if name == "joe":
    print("Your name rhymes with low.") 
else: 
    print(f"Hey {name}.") 
     

## 3
## Copy and modify the above example so that if the name is "dell", it will print "That’s a computer brand." 
     

## 4
## Try this.
age = 5
if age < 21: 
    print("You can't drink alcohol in the US yet.") 
else: 
    print("You are legally allowed to drink. Drink responsibly 😊 ") 
     

## 5
## Copy and modify the above example so that the legal drinking age is 40. (Just to be funny.) 

 

## 6
## Try this. Notice that it will ask for input. 
name = input("What is your name?") 
if name == "joe": 
    print("Your name rhymes with low.") 
else: 
    print(f"Hey {name}.") 

 
## 7
## Modify the above example so that if the name is "cobb", it will say "That’s a Ft Gordon building!" 

 
## 8 
## Try this. 
age = 10 
ageNextYear = age + 1 
print(ageNextYear) 
     

## 9
## Try this. Note: you will get an error. 
age = input("How old are you?") 
ageNextYear = age + 1 
print(ageNextYear) 
     

## 10 
## Try this. 
age = int(input("How old are you?")) 
ageNextYear = age + 1 
print(ageNextYear) 
     
## 11
## Copy and modify the previous example to do the following: 
## - Ask the user for age 
## - Say "You will be 65 years old in 11 years", but put the correct number instead of 11. 
     

## 12
## Try this. Note: you will get an error. 
age = input("How old are you?") 
if age < 21 : 
    print("You can't drink alcohol in the US yet.") 
else: 
    print("You are legally allowed to drink. Drink responsibly 😊 ") 
     

## 13
## Modify the above example so it works. You’ll use the `int` function. 

 
## 14
## Copy and modify the above example so that it shows how many years remain until you can drink (but only display that if you’re under the drinking age). 

 

## 15
## Write a program that takes a name from the user. If the name is the letter "A", say "Your name is just the letter A? That’s kinda cool".  Otherwise, say "Ok, your name is ___". 
     

## 16
## Try this: 
birthyear = 1998 
if birthyear < 2000: 
    print("You were born before 2000.") 
elif birthyear == 2000: 
    print("You were born in 2000.") 
else: 
    print("You were born after 2000.") 

 

## 17
## Modify the previous example to ask the user for year of birth (using input). 

 
## 18
## Ask the user how many French fries they want. Display different responses depending on how many they request. (Examples: "That’s way too many!", etc.) 

 
## 19
## Try this. Did it print what you expected?
x = 44 
if x < 20: 
    print("A") 
    print("B") 
print("C") 


## 20
## Modify the value of x in the previous example. Does it print what you expected? 


## 21
## Ask the user for a number.
## If the user gives a number more than 50, 
##    then ask "What is your name?"
##    and display "Hello" followed by the name.
## If the user gives any other number,
##    then ask "How did you pick that number?"
##    and regardless of what they say, display "I see."
## After all of that, say "Have a good day."


## 22
## Write a program that takes a number from the user. Display the number doubled. Then do a sequence of creative if statements of your choice. Some examples: if the number is greater than 30, display "that’s pretty big." If the number is negative, display "Really? Negative? Interesting".  

 
## 23
## Ask the user for the cost of a single item and the quantity purchased. Print the total cost. 

 
## 24
## Modify the previous example so that the shop gives a discount of 10% if you buy at least 20 of an item.  
## For example, if one item costs $5, and you’re buying 20, total cost would be $90. 
     

## 25
## Ask the user for a number. Print the absolute value of the number without using the abs function. 


## 26
## Ask the user for a temperature in Celsius, and display the temperature in Fahrenheit. 


## 27
## Same as previous example, but backwards. 


## 28
## Combine the two previous examples: ask the user for a number and which way to convert. 
          
## 29
## Try this:
name = input("What is your name? (type it lowercase please.)")
print("Ok, let me look up that name...")
if name == "bob":
    print("That name used to be common, I think.")
elif name == "sue":
    print("Your name also refers to a legal action.")
elif name == "rob":
    print("Another abbreviation for robert, correct?")
elif name == "lacy":
    print("Does the origin of your name relate to clothing with lace?")
else:
    print("I don't know you.")
print("Done.")

          
## 30
## Try this. How is it different from the previous example?
name = input("What is your name? (type it lowercase please.)")
print("Ok, let me look up that name...")
if name == "bob":
    print("That name used to be common, I think.")
if name == "sue":
    print("Your name also refers to a legal action.")
if name == "rob":
    print("Another abbreviation for robert, correct?")
if name == "lacy":
    print("Does the origin of your name relate to clothing with lace?")
else:
    print("I don't know you.")
print("Done.")
