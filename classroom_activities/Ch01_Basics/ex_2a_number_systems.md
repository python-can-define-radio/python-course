# Number Systems

ℹ️ This material coincides with material from python slideshow B (slides 10, 39). 

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

Note that functions work alone, but the format specifiers don't, unless you use the `format` function:

```python3
## This works:
exampleVar = bin(6)
print(f"The value is {exampleVar}.")

## This won't work:
exampleVar = {6:b}
print(f"The value is {exampleVar}.")

## This works:
exampleVar = format(6, "b")
print(f"The value is {exampleVar}.")
```

Also note that the format specifiers for other number systems work for integers, but don't work for floats:

```python3
item_number = 27.283
print(f"This will give an error, because item_number is a float: {item_number:b}.")
```
# IP addresses
ipv4 addresses use 32 total bits (4 "octets", 8 bits for each "octet") typically written in dotted decimal notation.  
example: 10.50.151.180  
which is the same as saying...  
00001010.00110010.10010111.10110100   
...to a computer  
each octet ranges from 0-255 which is 2⁸ available numbers
|     Host Bits    | Values | Total|
|:---------:|:------:|----------|
|  1   |  0 or 1	   | 2 or 2¹ |
|  2   |  00, 01, 10, 11	| 4 or 2² |
|  3   |  000, 001, 010, 011, 100, 101, 110, 111  | 8 or 2³ |
|  4   |  0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111,<br>1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111 | 16 or 2⁴ |
|  5   |  00000, 00001, 00010, 00011, 00100, 00101, 00110, 00111,<br>01000, 01001, 01010, 01011, 01100, 01101, 01110, 01111,<br>10000, 10001, 10010, 10011, 10100, 10101, 10110, 10111,<br>11000, 11001, 11010, 11011, 11100, 11101, 11110, 11111  | 32 or 2⁵ |
  

