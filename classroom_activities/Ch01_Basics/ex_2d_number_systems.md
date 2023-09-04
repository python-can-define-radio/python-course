# Number Systems

Sometimes, you may wish to display a number using a different number system.

Here's a table of a few examples:

|Decimal number (base 10) | Binary number (base 2) | Octal number (base 8) | Hexadecimal number (base 16) |
|--|--|--|--|
|1|1|1|1|
|2|10|2|2|
|3|11|3|3|
|25|11001|31|19|
|120|1111000|170|78|


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
