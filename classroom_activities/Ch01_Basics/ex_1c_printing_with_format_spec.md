# Printing with Format Specifiers

### Introduction

Sometimes, you want to print with some specific format.
For example:
 - Rounding a number to two decimal places
 - Padding a number with spaces so that it aligns with other numbers in a list
 - Displaying a number in another number system

ℹ️ This material coincides with material from python slideshow B (slides 12-15, 64-68). 

Here are some examples of how to specify the formatting when printing.

### Note:
- The "f" that preceeds the string, such as, f"hello", means ***format***.
- The "f" inside the curly braces, such as, {item_number:.2f}, means ***fixed-point notation***. That is, the number of decimal places is fixed.

```python3
## Example group 1
## Try these all at once.
item_number = 27.283
print()
print(f"My item num is {item_number}.")
print()
print(f"My item num is {item_number:10}. Notice that it is padded with spaces on the left.")
print()
print(f"My item num is {item_number:.2f}, rounded to two decimal places.")
print()
print(f"My item num is both rounded and has extra space: {item_number:9.2f}. Do you see?")
print()
print("You can also center the value within the available space.")
print("I'll add some letters before and after to make it clear:")
print(f"letters{item_number:^11.2f}letters")
print()
print(f"Here's how to left-align with some letters after for visual context: {item_number:<11.2f}letters")
```

```python3
## Example group 2
## Try these all at once.
another_num = 17
print("Here's how to display in binary, octal, hexadecimal:")
print(f"The number {another_num}, expressed in binary, is {another_num:b}.")
print(f"The number {another_num}, expressed in octal, is {another_num:o}.")
print(f"The number {another_num}, expressed in hexadecimal, is {another_num:x}.")

## Incidentally, the format code "d" means decimal, which is the default:
print(f"The number {another_num}, expressed in decimal, is {another_num:d}.")

## You can also display the number with a prefix that indicates the number system:
print(f"The number {another_num}, expressed in binary with a prefix, is {another_num:#b}.")
print(f"The number {another_num}, expressed in octal with a prefix, is {another_num:#o}.")
print(f"The number {another_num}, expressed in hexadecimal with a prefix, is {another_num:#x}.")
```

```python3
## Note that the format specifiers for other number systems don't work for floats:
item_number = 27.283
print(f"This will give an error, because item_number is a float: {item_number:b}.")
```

### Exercises
- Hint: Each of the exercises below will require at least one `input` "ask the user" statement,  and one `print` "display" statement.
```python3
# 1
# Ask the user a number. Display the number rounded to 3 decimal places.


# 2 
# Ask the user for the current cost-per-gallon of gasoline. Display the cost per pint, rounded to the nearest cent.
```

### For more information:
- This website gives some great practical examples. Recommended to start here.  
  https://www.linisnil.com/articles/practical-guide-to-python-string-format-specifiers/  
- Another good site.  
  https://www.pythonmorsels.com/string-formatting/  
- This website gives detailed documentation; somewhat more difficult to read.  
  https://docs.python.org/3/library/string.html#format-specification-mini-language

webpage for this lesson:  
https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch01_Basics/ex_2b_printing_with_format_spec.md
