<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 Jun 06: classroom_activities/Ch01_Basics/ex_2d_number_systems.md
2023 Dec 18: classroom_activities/Ch01_Basics/eex_2c_number_systems.md
2024 Feb 14: classroom_activities/Ch01_Basics/ex_2a_number_systems.md
</pre>
</details>


# Number Systems

[Rich Presentation for ex_2a-2b](https://raw.githubusercontent.com/python-can-define-radio/python-course/main/resources/rich_presentations/02c_02d_02e_number_systems_operators.py)

Sometimes, you may wish to display a number using a different number system.

Here's a table of a few examples:

|Decimal number (base 10) | Binary number (base 2) | Octal number (base 8) | Hexadecimal number (base 16) |
|--|--|--|--|
|1|1|1|1|
|2|10|2|2|
|3|11|3|3|
|25|11001|31|19|
|120|1111000|170|78|


ℹ️ This material coincides with material from python slideshow B (slides 10, 39). 

You can ask Python to do this for you:

```python3
print(bin(17))
print(oct(17))
```

you could also type

```python3
print(f"An arbitrary number in binary: {bin(17)}")
```

It will display the number as `0b10001`. The `0b` prefix is a way to remind you that this is a binary number.

If you prefer to not see that prefix, you could type

```python3
print(f"An arbitrary number in binary without a prefix: {17:b}")
```

-------------------

How about hexadecimal and octal?

```python3
print(f"An arbitrary number in octal: {oct(17)}")
print(f"An arbitrary number in octal without a prefix: {17:o}")
print(f"An arbitrary number in hexadecimal: {hex(17)}")
print(f"An arbitrary number in hexadecimal without a prefix: {17:x}")
```

---------------

Note that functions work alone, but the format specifiers don't:

```python3
## This works:
exampleVar = bin(6)
print(f"The value is {exampleVar}.")

## This won't work:
exampleVar = {6:b}
print(f"The value is {exampleVar}.")
```
