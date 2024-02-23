<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2024 Feb 05: resources/data_types.md     -- Make it a resource rather than a lesson.
2023 Jun 06: classroom_activities/Ch01_Basics/ex_7c_types.md    -- Move & rename to organize the course files.
</pre>
</details>

# Data Types
ℹ️ This material coincides with material from python slideshow B (slides 21-22).

Python variables can hold any of several types of data, e.g., an integer, a floating-point number, a string, a list, dictionary, etc.  Python can automatically detect and assign a "type" to a variable when the variable is defined, e.g.:
  `x = 2.5`  Assigns/defines x be a varible of type "float", having the value shown.
  `s = "1 GHz = 1 x 10^9 Hz"`  Assigns s to a string variable, having the value shown.

Python has functions for changing the type of a variable, e.g.,
  `x = int(x)` Reassigns x to be an integer, having the value: 2  (no decimal places).

Python includes a "type()" command to determine what kind of data is held in a variable or a value.  Examples are given below.


We know that the type of `a` in this first example is `int` (short for integer).

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
