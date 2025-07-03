## First ![python.png](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/python.png?raw=true)   Challenge the `in` keyword

Create a python function that checks a string to see whether a specific pattern (another string) is included in the larger string.
   - Do not use the `in` keyword. (Exception: you may use `for ___ in ___`.)
   - Do not use the `.contains()` method.
   - It should return a boolean value.
   - Write 3-5 assert statements to confirm functionality.

Example run:  
`print(does_it_contain("my dog creates his own textbooks", "creates"))`  # Should display True  
`print(does_it_contain("my dog creates his own textbooks", "eats"))`  # Should display False

## Second ![python.png](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/python.png?raw=true) Challenge min/max

Create a python function that:
   - Takes a `list` of integers and/or floats.
   - Do not use the `min()` or `max()` functions unless you create your own.
   - It should return the average of the highest and lowest number of the list.
   - Write 3-5 assert statements to confirm functionality.

Example run:  
`print(avg_high_low([50, 61, 100]))`   # the average of 100 and 50 should display 75

## Third ![python.png](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/python.png?raw=true) Challenge use prompt_toolkit


Convert any of your practical exercises to use the prompt_toolkit module.
   - Lesson on prompt_toolkit available [here](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/02_prompt_toolkit.md).
   - For more information and tutorials go to the [prompt_toolkit docs](https://python-prompt-toolkit.readthedocs.io/en/master/pages/getting_started.html#getting-started).

## Fourth ![python.png](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/python.png?raw=true) Challenge turtle challenge


Draw the following image (or select your own image) using the turtle module.
   - More turtle examples available [here](https://github.com/python-can-define-radio/python-course/tree/main/classroom_activities/Ch03_Misc_examples/turtle_ex).
   - For more information and tutorials go to the [turtle docs](https://docs.python.org/3/library/turtle.html).

![python.png](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/s_challenge.png?raw=true)

## Fifth ![python.png](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/python.png?raw=true) Challenge julian date


Create a python function that:
   - Takes 3 integer parameters: year, month, day.
   - Returns a tuple `(a, b)` where
     - `a` is a boolean that is True if that year is a leap year, and False otherwise.
     - `b` is the Julian date as an integer
   - Write 3-5 assert statements to confirm functionality.

Example run:  
`print(julian(2000, 6, 16))`  # Should display (True, 137)
`print(julian(2001, 6, 16))`  # Should display (False, 136)

## Sixth ![python.png](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/python.png?raw=true) Challenge Remove only unecessary whitespace


Write a function that:
   - Is called strip_each_line and takes a single string argument.
   - Returns the argument without leading and trailing whitespace
   - Keeps the line endings the same as the original string (not all operating systems use "\n" for newline)
   - Mirrors the behavior of the function inspect.cleandoc(), which keeps certain indentation.
 
Example run:  
`print(strip_each_line("  abc    \n   def   "))`  # Should display "abc\ndef"

## Seventh ![python.png](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/python.png?raw=true) Challenge 

## Make a function that says the age of a given person.

def ageof(name):
     if name == "Jaime":
         return 32
     elif name == "Taelor":
         return 34
     else:
         raise NotImplementedError()

# print(ageof("Jaime"))   ## should print 32
# print(ageof("Taelor"))  ## should print 34


# 2a  Make a function named `whichlower` that returns "first arg was lower" or "second arg was lower"

@typechecked
def whichlower(fir: float, snd: float) -> str:
    if fir > snd:
        return "Second lower"
    elif fir < snd:
        return "First lower"
    elif fir == snd:
        return "Is Equal"   
    else:
        return "is Not a regular number"
    

assert whichlower(3, 7) == "First lower"
assert whichlower(8, 5) == "Second lower"
assert whichlower(7, 3) == "Second lower"
assert whichlower(1, 9) == "First lower"
assert whichlower(1, -9) == "Second lower"
assert whichlower(1.3, -9) == "Second lower"
assert whichlower(1, 1) == "Is Equal"
assert whichlower(3, 0b011) == "Is Equal"
if "do not run this" == "please":
    # Cannot run this because `bin(3)` is a string.
    assert whichlower(3, bin(3)) == "Is Equal"


# # 2b Make a function that, given two numbers, returns "lowest was ___"


def lowerwas(fir, snd):
    if fir > snd:
        return f"the lowest of two was {snd}"
    elif fir < snd:
        return f"the lowest of the two is {fir}"
    

print(lowerwas(3, 7))
print(lowerwas(40, 23))
# assert lowerwas(3, 7) == "lowest was 3"
# assert lowerwas(8, 5) == "lowest was 5"



# 2c Make a function that returns the lower of two numbers.
# Tests:

def smaller(fir, snd):
     print("fir is", fir, "and snd is", snd)
     if fir < snd:
         return 3 
     if snd < fir:
         return 4


print(smaller(3, 7))  # should display 3
print(smaller(9, 4))  ## should display 4
print(smaller(12, 15))  ## should display 12
