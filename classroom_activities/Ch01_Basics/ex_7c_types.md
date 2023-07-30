## Types

We know that the type of `a` in this example is `int` (short for integer).

```python3
a = int(input("How old are you? "))
print(f"Next year, you'll be {a + 1} years old.")
```

We know that Python can tell us the type:

```python3
print(f"The type of that variable is {type(a)}")
```

And that feature can be useful in other cases:

```python3
b = input("What is your name? ")
c = "hello"
d = 3
e = 3.1
f = 3.0
print("The types of those variables are...")
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
```

The `type()` function is especially useful when you're dealing with types that aren't strings, integers, or floats:

```python3
words = ["The", "elements", "are", "strings", "but", "this", "is", "a", "list"]
print(type(words))
```

Now, what if we set a variable equal to something that uses the "greater than" operator?

```python3
temp_in_degrees_f = 101.2
isHigherThanNormal = (temp_in_degrees_f > 98.6)   
print(f"Is the temperature {temp_in_degrees_f} higher than normal? The answer is... {isHigherThanNormal}")

another_temp = 98.5
isHigherTwo = (another_temp > 98.6)
print(f"Is the temperature {another_temp} higher than normal? The answer is... {isHigherTwo}")
```

<details><summary><i>Note (click)</i></summary>
The parentheses are optional; the author believes they improve readability.  
  In other words, <code>x = (y > 3)</code> is the same as <code>x = y > 3</code>.
</details>

As you can see, it shows either `True` or `False`. Those might look like strings, but they aren't:

```python3
temp_in_degrees_f = 101.2
isHigherThanNormal = (temp_in_degrees_f > 98.6)
print(f"The type of isHigherThanNormal is {type(isHigherThanNormal)}")
print(f"The type of True (the value, not the string) is {type(True)}")
```

Python calls them 'bool', which is short for 'boolean'.
As you'll find documented on thousands of websites, a boolean value is simply a value that can only be True or False.

That can be useful when dealing with complex logic, as it allows the parts of the logic to be named. For example, these two are equivalent:

```python3
## First example:
shirtStatus = input("Are you wearing a shirt? ")
shoesStatus = input("Are you wearing shoes? ")
temp = float(input("What is your temperature? "))
if shirtStatus.lower() == "yes" and shoesStatus.lower() == "yes" and temp < 100.3:
    print("You can have service.")

## Second example:
shirtStatus = input("Are you wearing a shirt? ")
shoesStatus = input("Are you wearing shoes? ")
temp = float(input("What is your temperature? "))
hasShirt = (shirtStatus.lower() == "yes")
hasShoes = (shoesStatus.lower() == "yes")
safeTemp = (temp < 100.3)
if hasShirt and hasShoes and safeTemp:
    print("You can have service.")
```
