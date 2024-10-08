
# Variable names

ℹ️ This material coincides with material from python slideshow B (slides 24, 54-63). 

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
###########################   
# invalid variable names: #   
###########################

## These four examples will cause errors ensure they are commented out before you move on.

## Can't use keywords, as an example: 
if = 6

## Can't start with number
3rdthing = "hi"

## Can't have spaces inside of the name
my var = 3

## Can't have special characters (only "_" is allowed inside a variable name)
$d = 6
```


#### Valid but not recommended

```python3
## This definition of a variable is valid, but please don't, because "input" will no longer be a function.
input = 7

``` 

