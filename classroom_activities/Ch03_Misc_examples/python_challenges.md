## First ![python.png](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/python.png?raw=true)   Challenge the `in` keyword

Create a python function that checks a string to see whether a specific pattern (another string) is included in the larger string.
   - Do not use the `in` keyword. (Exception: you may use `for ___ in ___`.)
   - Do not use the `.contains()` method.
   - It should return a boolean value.
   - Write 3-5 assert statements to confirm functionality.

example run:  
`print(does_it_contain("my dog creates his own textbooks", "creates"))`  # Should display True  
`print(does_it_contain("my dog creates his own textbooks", "eats"))`  # Should display False

## Second ![python.png](https://github.com/python-can-define-radio/python-course/blob/main/resources/misc/python.png?raw=true) Challenge min/max

Create a python function that:
   - Takes a `list` of integers and/or floats.
   - Do not use the `min()` or `max()` functions unless you create your own.
   - It should return the average of the highest and lowest number of the list.
   - Write 3-5 assert statements to confirm functionality.

example run:  
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

example run:  
`print(julian(2000, 6, 16))`  # Should display (True, 137)
`print(julian(2001, 6, 16))`  # Should display (False, 136)
