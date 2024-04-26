# Dataclasses

ℹ️ This material coincides with material from python slideshow D (slides 16-30).

### Exercises
This lesson shows how to use Python's dataclasses module to group related data in a single data structure.

```python3
## 1
## Try this.
from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    age: int
    breed: str
   
d1 = Dog("Tucker", 4, "Cocker Spaniel")
d2 = Dog("Henry", 8, "Bassett Hound")
# You have the option of using named keyword arguments:
d3 = Dog(name="Henry", age=8, breed="Bassett Hound")

print(d1.name)
```

In this example, `Dog` is a "class", which can be thought of as a template that describes what data we want to include every time we use the `Dog` class.

The variables `d1` and `d2` are called "instances" of the class `Dog`. It's also possible to call them "objects".

So far, this doesn't provide any new features, but it allows you to organize data into named attributes. It also ensures that every `Dog` object that you create (or _instantiate_) has the required attributes: `name`, `age`, and `breed`.

```python3
## 2
## Fill in the blanks:
print(f"The dog named {d1.name} is {___} years old. His/her breed is {___}.")
```

Dataclasses are particularly useful when paired with lists: 

```python3
## 3
## Try this.
from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    age: int
    breed: str

dogs = [
    Dog("Tucker", 4, "Cocker Spaniel"),
    Dog("Henry", 8, "Bassett Hound")
]

print("The first item of our dogs list:")
print(dogs[0])
print("The name of the first dog:")
print(dogs[0].name)
```

You'll see more examples of using lists with dataclasses in the next lesson.

```python3
## 4
## Make a Car class that has at least three attributes.
## Make a list of at least three Car objects (a.k.a. instances).
########################
##  INSTRUCTOR-CHECK  ##
########################
```

<details>
<summary>Optional exercises (click to expand...)</summary>

#### Using lists of objects

Often, you may work with related sets of data. For example, imagine a list of instructors that includes their names, ages, and years of experience. One way to express this data is a list of objects. In the example below, you'll see that we create a dataclass called `Instructor`, and we create a list of five `Instructor` objects. Each object is an "instance" of the class `Instructor`.

```python3
## 5
from dataclasses import dataclass

@dataclass
class Instructor:
    name: str
    age: int
    yearsExp: int

instructors = [
    Instructor("Maria", 38, 7),
    Instructor("Walton", 47, 22),
    Instructor("Martin", 52, 18),
    Instructor("Joel", 28, 3),
    Instructor("Tate", 67, 5)
]
```

You could use this in a `for` loop like so:

```python3
print("Here is my instructor data:")
for person in instructors:
    print(f"The instructor {person.name} is {person.age} years old and has {person.yearsExp} years of experience.")
```

Let's do some math inside of the loop.

```python3
## 6
## Given the instructors list defined above,
## display how old each person was when he/she started this job.
## For example, Maria started this job 7 years ago, so you would print this:
##    The instructor Maria is 38 years old, and started working at age 31.
##
## Note: for this exercise, you cannot add any attributes to the dataclass.
## In other words, this portion must remain unchanged:
@dataclass
class Instructor:
    name: str
    age: int
    yearsExp: int
## Why? The goal is to have Python compute the
## started-working-age within the `for` loop.
## Ask an instructor if this is unclear.  


## 7 
## Copy and modify the previous example. In this version, for each instructor,
## display the following:
##     The instructor Maria has been working for 7 years, and will receive a $70 bonus this year.
## 
## The bonus must be $10 times the number of years of experience (5 years would be $50, etc).
## As in the previous exercise, the dataclass must remain unchanged.


## 8
## Copy and modify the previous example.
## Ask the user for the extra bonus per year of experience. Compute appropriately.
## Example run:
##     What is the bonus per year of experience? 20
##     The instructor Maria has been working for 7 years, 
##     and will receive a $140 bonus this year.
##     The instructor Walton has been working for 22 years,
##     and will receive a $440 bonus this year.
##     ...etc...


## 9
## Copy and modify the previous example.
## After the for loop, display
##    "The total amount of work experience for this team is ___". 
## Must compute the total inside the for loop.
## Hint: the structure will resemble this:
##   totalYearsExp = 0
##   for ??? in ???:
##       totalYearsExp += person.yearsExp
##   print(f"The total amount of work experience for this team is {totalYearsExp}")
```


# Classes using `pydantic` module

This section of the lesson shows how to use an external module to verify and enforce **types** in a class definition.

Prerequisite: 
```sh
## Run this in the terminal:
pip install pydantic
```

```python3
## 10
## Try this.
from pydantic import BaseModel

class Dog(BaseModel):
    name: str
    age: int
    breed: str
   
d1 = Dog(name="Tucker", age=4, breed="Cocker Spaniel")
d2 = Dog(name="Henry", age=8, breed="Bassett Hound")

print(d1.name)
```

The line `class Dog(BaseModel)` means that `Dog` will **inherit** the behavior of `BaseModel`.  
`BaseModel` differs from the `@dataclass` decorator in a few ways:

- It forces us to use keyword arguments when **instantiating** the class.
- It enforces correct types.

```python3
## 11
## Copy and modify the previous exercise to confirm that the `types` are being enforced.
## Change one of the three defined parameters either `str` to `int` or `int` to `str` and run it.
```
This should have given you a useful error something like this:

```sh
Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='Tucker', input_type=str]
```
or this:

```sh
Input should be a valid string [type=string_type, input_value=4, input_type=int]
```

One useful feature of pydantic...

```python3
## 12
## Try this. Do you expect this to run?
d4 = Dog(name="Fred", age="5", breed="Greyhound")

print(d4.age)
print(d4.age + 1)
```

Notice that our string "5" is converted to an integer without ever writing `int()`.  
This is Pydantic's [default behavior](https://docs.pydantic.dev/latest/concepts/models/#data-conversion) — when the data can be converted to the type specified in the class definition, it will be converted silently.

```python3
## 13
## Using pydantic's `BaseModel`, make any class that has at
## least three attributes with various types.
## Make a list of at least three objects.
```

For more information, see the [pydantic docs](https://docs.pydantic.dev/latest/).
</details>
