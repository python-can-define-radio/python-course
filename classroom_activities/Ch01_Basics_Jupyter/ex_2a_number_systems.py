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
# # Number Systems
#
# ℹ️ This material coincides with material from python slideshow B (slides 10, 39). 
#
# Sometimes, you may wish to display a number using a different number system.
#
# Here's a table of a few examples:
#
# |Decimal number (base 10) | Binary number (base 2) | Octal number (base 8) | Hexadecimal number (base 16) |
# |--|--|--|--|
# |1|1|1|1|
# |2|10|2|2|
# |3|11|3|3|
# |25|11001|31|19|
# |120|1111000|170|78|

# %% [markdown]
# You can ask Python to do this for you:

# %%
print(bin(17))
print(oct(17))

# %% [markdown]
# you could also type

# %%
print(f"An arbitrary number in binary: {bin(17)}")

# %% [markdown]
# It will display the number as `0b10001`. The `0b` prefix is a way to remind you that this is a binary number.
#
# If you prefer to not see that prefix, you could type:

# %%
print(f"An arbitrary number in binary without a prefix: {17:b}")

# %% [markdown]
# How about hexadecimal and octal?

# %%
print(f"An arbitrary number in octal: {oct(17)}")
print(f"An arbitrary number in octal without a prefix: {17:o}")
print(f"An arbitrary number in hexadecimal: {hex(17)}")
print(f"An arbitrary number in hexadecimal without a prefix: {17:x}")

# %% [markdown]
# Note that functions work alone, but the format specifiers don't, unless you use the `format` function:

# %%
## This works:
exampleVar = bin(6)
print(f"The value is {exampleVar}.")

# %%
## This won't work:
exampleVar = {6:b}
print(f"The value is {exampleVar}.")

# %%
## This works:
exampleVar = format(6, "b")
print(f"The value is {exampleVar}.")

# %% [markdown]
# Also note that the format specifiers for other number systems work for integers, but don't work for floats:

# %%
item_number = 27.283
print(f"This will give an error, because item_number is a float: {item_number:b}.")
