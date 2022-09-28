"""Example 2b Printing with Format Specifiers
   webpage for this lesson: "https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/ex_2b_printing_with_format_spec.py"
"""

## Sometimes, you want to print with some specific format.
## For example:
##  - Rounding a number to two decimal places
##  - Padding a number with spaces so that it aligns with other numbers in a list

## For example:
item_number = 27.283
print(f"My item num is {item_number}.")
print(f"My item num is {item_number:10} and I put some space with it.")
print(f"Rounded would be {item_number:.2f} with two decimal places.")

## This website gives some great practical examples. Recommended to start here.
## https://www.linisnil.com/articles/practical-guide-to-python-string-format-specifiers/

## Another good site:
## https://www.pythonmorsels.com/string-formatting/

## This website gives detailed documentation; somewhat more difficult to read.
## https://docs.python.org/3/library/string.html#format-specification-mini-language




