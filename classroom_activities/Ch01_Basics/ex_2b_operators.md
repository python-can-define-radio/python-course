<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2022 Aug 05: classroom_activities/ex_2b_operators.md
2023 Jun 06: classroom_activities/ex_2e_operators.md
2023 Mar 10: classroom_activities/Ch01_Basics/ex_2e_operators.md
2024 Feb 14: classroom_activities/Ch01_Basics/ex_2b_operators.md
</pre>
</details>


# Python arithmetic operators

Most people are familiar with these four operators: +, -, *, /

In this exercise, you'll learn some other useful operators: //, %, **

ℹ️ This material coincides with material from python slideshow B (slides 26-32). 

### Exercises

```python3
## 1
## Try this example

x = 13 / 5
print(x, "is the result of 13 / 5 using regular division.")

y = 13 // 5
print(y, "is the result of 13 // 5 sometimes called floor division.")

z = 13 % 5
print(z, "is the result of 13 % 5 sometimes called modulus or the remainder.")

print(f"So 13 divided by 5 gives you {x};")
print(f"Using floor division (13 // 5) drops the remainder giving you {y}.")
print(f"The modulus operator (%) gives you only the remainder of the operation ({z}).")
print(f"This represents 3 fifths or 3/5 which equals {z/5}")

a = 2 ** 5
print(a, "is the result of 2 ** 5, or 2 to the 5th power.")
print("5 is the exponent, so this can be called exponentiation.")
print("The (**) operator gives 2 to the power of 5 or 2*2*2*2*2")

## 2
## Now let's incorporate some inputs.
## Ask the user for two numbers.
## Display "If you divided ___ by ___, then you
## would get ____ with a remainder of ___".


## 2a
## Here's a real life example:
pieces_of_candy = 23
people = 5

candy_per_person = pieces_of_candy // people
leftover = pieces_of_candy % people
print(f"If you had {pieces_of_candy} pieces of candy,")
print(f"and you wanted to share it with {people} people,")
print(f"each person would get {candy_per_person} pieces,")
print(f"andthere would be {leftover} leftover.")


## 3
## Calculating an exponent
## Ask the user for two numbers.
## Display "If you computed ___ to the power of ___, then you would get ___."
## (Hint: What is the operator for exponent in Python? It may not be what you think.)


## 4
## Operators that may not do what you expect
## Based on question #1, does % calculate a percentage? (Answer: No)
## Based on question #2, does ^ calculate an exponent? (Answer: No)

```

Let's also explore some more advanced uses of the assignment operator, that is, the equals sign:

```python3

## 5
## Try this. As you can see, it's possible to reassign variables.
x = 3
print("Currently, x is...")
print(x)
x = 4
print("Now, x is...")
print(x)


## 6
## Try this. It's a little counter-intuitive.
x = 3
print("Currently, x is...")
print(x)
## You should read the line below as "Set x to 5 more than what x used to be."
x = x + 5
print("Now, x is...")
print(x)


## 7
## Python provides another equivalent way to do this:
x = 3
print("Currently, x is...")
print(x)
x += 5
print("Now, x is...")
print(x)

```

### Special ways to type numbers

You can type large or small numbers using an `e`:

```python3
x = 2e3
print(x)  # This will print 2000.0, which is a float
```

You can insert underscores for readability:
```python3
y = 2_000
print(y)  # This will print 2000, which is an integer
```
