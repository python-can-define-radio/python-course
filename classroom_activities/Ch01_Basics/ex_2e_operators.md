Most people are familiar with these four operators: +, -, *, /

In this exercise, you'll learn some other useful operators: //, %, **


```python3
## 1
## Try this example

x = 13 / 5
print(x, "is the result of 13 / 5 using regular division.")

y = 13 // 5
print(y, "is the result of 13 // 5 sometimes called floor division.")

z = 13 % 5
print(z, "is the result of 13 % 5 sometimes called modulus or the remainder.")

print(f"So 13 divided by 5 gives you {x}, using floor division (13 // 5) drops the remainder giving you {y}.")
print(f"The modulus operator (%) gives you only the remainder of the operation ({z}).)
print(f"This represents 3 fifths or 3/5 which equals {z/5}")

a = 2 ** 5
print(a, "is the result of 2 ** 5 or 2 to the 5th power sometimes called exponentiation.")
print("The (**) operator gives 2 to the power of 5 or 2*2*2*2*2")

## 2
## Now let's incorporate some inputs.
## Ask the user for two numbers.
## Display "If you divided ___ by ___, then you would get ____ with a remainder of ___".


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
