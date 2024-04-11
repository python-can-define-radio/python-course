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

# Classes using `pydantic` module

This section of the lesson shows how to use an external module to verify and enforce **types** in a class definition.

Prerequisite: 
```sh
## Run this in the terminal:
pip install pydantic
```

```python3
## 5
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
## 6
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
## 7
## Try this. Do you expect this to run?
d4 = Dog(name="Fred", age="5", breed="Greyhound")

print(d4.age)
print(d4.age + 1)
```

Notice that our string "5" is converted to an integer without ever writing `int()`.  
This is Pydantic's [default behavior](https://docs.pydantic.dev/latest/concepts/models/#data-conversion) — when the data can be converted to the type specified in the class definition, it will be converted silently.

```python3
## 8
## Using pydantic's `BaseModel`, make any class that has at
## least three attributes with various types.
## Make a list of at least three objects.
```

For more information, see the [pydantic docs](https://docs.pydantic.dev/latest/).
