# ---
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Modules
#
# ℹ️ This material coincides with material from python slideshow D (slides 4-15).
#
# In Python, modules are packets of code that enhance the operation of Python.
# Modules may include multiple Python functions, each giving a specific functionality.
# E.g., the "math" modules includes functions such as "sqrt()" and "cos()" 
# Using an "import" command, modules may be added to a program to make the module's functionality available to the program.
#
# When importing modules, there are a few approaches you can use:
#
# Import the whole module:

# %%
import math
print(math.sqrt(5))

# %% [markdown]
# Import one function:

# %%
from math import sqrt
print(sqrt(5))

# %% [markdown]
# Import the whole module, and give it another name ("alias"):

# %%
import math as m
print(m.sqrt(5))

# %% [markdown]
# Import everything from the module:

# %%
from math import *
print(sqrt(5))

# %% [markdown]
# # Printing with Format Specifiers
#
# ℹ️ This material coincides with material from python slideshow B (slides 12-15, 64-68). 
#
# Sometimes, you want to print with some specific format.
# For example:
#  - Rounding a number to two decimal places
#  - Padding a number with spaces so that it aligns with other numbers in a list
#  - Displaying a number in another number system
#
# ### Note:
# - The "f" that preceeds the string, such as, f"hello", means ***format***.
# - The "f" inside the curly braces, such as, {item_number:.2f}, means ***fixed-point notation***. That is, the number of decimal places is fixed.
#
# Here are some examples of how to specify the formatting when printing.

# %%
## 1
## Try this.
item_number = 27.286
print("My item num is", item_number, ".")
print("My item num is", format(item_number, ".2f"), "rounded to two decimal places.")

# %% [markdown]
# Here's how to do the same using f-strings.

# %%
## 2
## Try this.
item_number = 27.286
print(f"My item num is {item_number}.")
print(f"My item num is {item_number:.2f}, rounded to two decimal places.")

# %%
## 3
## Ask the user a number.
## Display the number rounded to 3 decimal places.


# %%
## 4
## Ask the user for the current cost-per-gallon of
## gasoline. Display the cost per pint,
## rounded to the nearest cent.

#######################
## INSTRUCTOR CHECK
#######################

# %% [markdown]
# You can also use format specifiers to add leading spaces. Notice that this allows things like prices to be vertically aligned on the decimal place.

# %%
## 5
apple_price = 1.78
something_expensive = 1062.02
guitar_price = 162.17
print("Prices:")
print(f"{apple_price:8}")
print(f"{something_expensive:8}")
print(f"{guitar_price:8}")

# %% [markdown]
# <details><summary>For more information:</summary>
#  
# - This website gives some great practical examples. Recommended to start here.  
#   https://www.linisnil.com/articles/practical-guide-to-python-string-format-specifiers/  
# - Another good site.  
#   https://www.pythonmorsels.com/string-formatting/  
# - This website gives detailed documentation; somewhat more difficult to read.  
#   https://docs.python.org/3/library/string.html#format-specification-mini-language
#   
# </details>

# %% [markdown]
#
