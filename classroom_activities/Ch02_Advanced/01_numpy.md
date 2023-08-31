https://numpy.org/doc/stable/user/absolute_beginners.html#numpy-the-absolute-basics-for-beginners

## 1. create a numpy array from a list

- Basic example.

```python3
    import numpy as np

    y = np.array([1, 3, 5, 6, 12, 32])
    print(y)

```

## 2. linspace function (endpoint=True or False)`np.linspace`

- np.linspace(start, stop, num=50, endpoint=True)  
    - Returns `num` evenly spaced samples, calculated over the interval `start, stop`. (defaults to 50 samples if not specified)
    - The endpoint of the interval can optionally be excluded `endpoint=False`.
 
```python3

    import numpy as np

    y = np.linspace(0, 5, 10, endpoint=True)
    print(y)

```

This will create an evenly spaced array of 10 data points between 0 and 5 including 5 as the last data point.  
If endpoint=False was used it would give an array of 10 evenly spaced data points between 0 and 4.5 (not including the stop of 5).  
An optional approach would be to use `np.arange` which is similar to linspace, but uses a step size (instead of the number of samples).

```python3
    ## To create the same array as the previous example with endpoint=False
    import numpy as np

    y = np.arange(0, 5, .5)
    print(y)

```

## 3. dtype=

The type of the output array. If dtype is not given, the data type is inferred from start and stop.  
The inferred dtype will never be an integer; float is chosen even if the arguments would produce an array of integers.  
If we force the issue by using `dtype=int` when the result would produce floats it will still work but may create some unintended outcomes.

```python3

    import numpy as np

    y = np.linspace(0, 5, 10, endpoint=False, dtype=int)
    print(y)

```

## 4. operations on an array (+,-,*,/) using a constant (addition, subtraction, division by a constant does not work on lists)

   - ### multiplying for a list
```python3 
    y = [4, 5, 6]  
    z = 3 * y
    print(z)
```
z is now `[4, 5, 6, 4, 5, 6, 4, 5, 6]` repeats all elements 3 times
   
   - ### multiplying for an array
```python3
    y = np.array([4, 5, 6])  
    z = 3 * y
    print(z)
```
z is now `np.array([12, 15, 18])` multiplies each element by 3
   
   - ### adding for an array (cannot be done with lists)
```python3
    x =np.array([3, 8, 15])  
    z = x + 3  
    print(z)
```
z is now `np.array[6, 11, 18]` adds to each element by the constant
   
   - ### subtracting for an array (cannot be done with lists)
```python3
    x =np.array([3, 8, 15])  
    z = x - 3
    print(z)
```
z is now `np.array[0, 5, 12]` subtracts from each element by the constant
   
   - ### dividing for an array (cannot be done with lists)
```python3 
    x =np.array([3, 9, 18])  
    z = x / 3
    print(z)
```
z is now `np.array[1., 3., 6.]` divides from each element by the constant (produces floats)
   
## 5. Performing operations on lists or arrays (multiplication, subtraction, and division do not work on lists)

   - ### adding for a list
```python3 
    x = [5, 6, 7]  
    y = [8, 9, 10]  
    z = x + y
    print(z)
```
z is now `[5, 6, 7, 8, 9, 10]` creates new list with all elements from each list
   
   - ### adding for an array
```python3   
    x = np.array([5, 6, 7])  
    y = np.array([8, 9, 10])  
    z = x + y
   print(z)
```
z is now `np.array([13, 15, 17])` adds each element to its counterpart same index
   
   - ### subtracting for an array (cannot be done with lists)
```python3
    x =np.array([3, 8, 15])  
    y =np.array([1, 2, 3])  
    z = x - y
   print(z)
```
z is now `np.array([2, 6, 12])` subtracts counterpart same index element from first array element
   
   - ### multiplying for an array (cannot be done with lists)
```python3
    x = np.array([5, 6, 7])  
    y = np.array([8, 9, 10])  
    z = x * y
    print(z)
```
z is now `np.array([40, 54, 70])` multiplies each element to its counterpart same index
    
   - ### dividing for an array (cannot be done with lists)
```python3
    x =np.array([3, 8, 15])  
    y =np.array([1, 2, 3])  
    z = x / y
    print(z)
```
z is now `np.array([3., 4., 5.])` divides elements in first array to its counterpart index in other array (produces float)
   
## 6. concatenate arrays (np.concatenate) forces appending arrays instead of adding each element
```python3
    x =np.array([3, 9, 18])  
    y =np.array([64, 7, 12])  
    z = np.concatenate([x, y])
    print(z)
``` 
z is now `np.array[3, 9, 18, 64, 7, 12]`
   
## 7. == with arrays

```python3
    import numpy as np


    ## 1
    a = 5
    b = 6
    print(a == b)

    ## 2
    a = 5
    b = 5
    print(a == b)

    ## 3
    x = [1, 2, 3]
    y = [1, 2, 4]
    print(x == y)

    ## 4
    xa = np.array([1, 2, 3])
    ya = np.array([1, 2, 4])
    print(xa == ya)
    areAllEqual = (xa == ya).all()
    print(areAllEqual)

    ## 5
    xa = np.array([3, 2, 1])
    ya = np.array([5, 0, 4])
    print(xa > ya)

    ## 6
    xa = np.array([4, 3, 1])
    print(xa > 2)

    ## 7
    ## this will give an error
    x =np.array([3, 9, 18])
    y =np.array([64, 7, 12])
    if x == y:
         print("same")
    else:
         print("different")

```
