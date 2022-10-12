# Example 2c Variables -- Python Practice 
webpage for this lesson: https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/ex_2b_printing_with_format_spec.py

In programming languagues, variables are allocations of computer memory assigned to store data 
for later use in the program. The programer chooses a name for the variable and sets it equal 
to a fixed values, a calculated value, or --to get input from a user-- an input statement.  The
variable (i.e., its name) can be used again later in the program to perform a calculation, to 
set a parameter for a function, or to print a result to the user on a display screen or in a data
file, as examples.

<details> <summary> Basic Rules for naming variables in Python3: (Click to expand.) </summary>

1. In general, the programer may select characters from any of these four groups: A-Z, a-z, 0-9, 
   and underscore (_).  However, these additional rules should be remembered:
2. Start the variable name with a letter or an underscore character, not a number.
3. Both lower case or capital letters may be used, but you'll need to be consistent
   when you use the variable later in your program.
4. After the first character in the variable's name, numbers may also be used.  
5. Do not use a "keyword" defined by Python, e.g. "in", "if", "not", "and", "while", etc.
6. Do not use the name of built-in function of Python, e.g., "print", "input", etc.  The Python 
   interpreter program will not prevent you from using them, but the orginal function will cease to work.

References for naming rules/conventions for variables in Python:  
~ https://pythonguides.com/python-naming-conventions/  
~ https://www.w3schools.com/python/gloss_python_variable_names.asp
 </details>

```python3
## EXERCISES ------------------------------------------------------------------------
## Valid variable names -- These are examples of valid variable assignment statements:
mynumber = 7
temp_in_f = 8.3
my2ndthing = "hi"
x3 = "stuff"
_myStuff = 7
result = mynumber * _myStuff

# This definition of a variable is valid, but please don't, because "input" will no longer be a function.
input = 7

#############
# invalid:
#############

# Can't use keywords, as an example: 
if = 6
# (After trying the previous line, delete it, or convert it to a comment by proceeding it with a number/pound symbol (#).)

# Can't start with number
3rdthing = "hi"

# Can't have spaces inside of the name
my var = 3

# Can't have special characters (only "_" is allowed inside a variable name)
$d = 6

## Using variables: 
## These statements reference/use the vaiables defined in the "Valid variable names" section, above.
print(mynumber)
print("The recorded temperature is", temp_in_f, "deg. F")
print(f"The following message was received '{my2ndthing}'.")
print(f"The result of multiplying {mynumber} and {_myStuff} is equal to {result}.")
```
