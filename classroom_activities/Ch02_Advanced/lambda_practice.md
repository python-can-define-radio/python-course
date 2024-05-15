```python3
## 1
## Try this.
def double(num):
    return num * 2

def triple(num):
    return num * 3

print("Result: ", double(2))
print("Result: ", triple(3))
```

```python3
# same as basic function but using lambda
# notice we use it just like a function in the print
doub = lambda p: p*2
trip = lambda u: u*3
print("Result: ", doub(2))
print("Result: ", trip(3))
```

```python3
# creating our own math function that uses another function
def domath(fn, x):
    return fn(x)

print("Result: ", domath(double, 2))
print("Result: ", domath(triple, 3))
```

```python3
# same thing using lambda directly as your function
mymath = domath(lambda z: z*6, 5)
print("Result: ", mymath)
```

```python3
# list comprehension and filtering directly with lambda
x = [3 ,5, 2, 4, 7, 3]
y = [i*2 for i in x]
z = [i for i in x if i > 3]
print("Original list: ", x)
print("List doubled: ", y)
print("Filtered list: ", z)
```

```python3
# using filter class with lambda
filtlist = list(filter(lambda num: num>5, x))
print("Filtered list: ", filtlist)
```

```python3
# creating our own filter
def filter(fn, p):
    z = []
    for i in p:
        if fn(i) == True:
            z.append(i)
    return z

print("Filtered list: ", filter(lambda z: z<=3, x))
```
