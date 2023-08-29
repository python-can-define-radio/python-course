https://numpy.org/doc/stable/user/absolute_beginners.html#numpy-the-absolute-basics-for-beginners

Outline:
1. create a numpy array from a list
2. linspace function (endpoint=True or False)(np.linspace)
3. dtype=
4. operations on an array (+,-,*,/) with a constant not to be confused with math operators
   # multiplying for a list
   y = [4, 5, 6]
   z = 3 * y  # z is now [4, 5, 6, 4, 5, 6, 4, 5, 6] repeats all elements 3 times
   # multiplying for an array
   y = np.array([4, 5, 6])
   z = 3 * y  # z is now np.array([12, 15, 18]) multiplies each element by 3
   # adding for an array
   x =np.array([3, 8, 15])
   z = x + 3  # z is now np.array[6, 11, 18] adds to each element by the constant
   # subtracting for an array
   x =np.array([3, 8, 15])
   z = x - 3  # z is now np.array[0, 5, 12] subtracts from each element by the constant
   # dividing for an array
   x =np.array([3, 9, 18])
   z = x / 3  # z is now np.array[1., 3., 6.] divides from each element by the constant
   # addition, subtraction, division by a constant does not work on lists
6. adding arrays together (multiplying, subtraction, division do not work for lists)
   # for a list
   x = [5, 6, 7]
   y = [8, 9, 10]
   z = x + y  # z is now [5, 6, 7, 8, 9, 10] creates new list with all elements from each list 
   # for an array
   x = np.array([5, 6, 7])
   y = np.array([8, 9, 10])
   z = x + y  # z is now np.array([13, 15, 17]) adds each element to its counterpart same index
8. multiplying arrays together cannot be done with lists
   x = np.array([5, 6, 7])
   y = np.array([8, 9, 10])
   z = x * y  # z is now np.array([40, 54, 70]) multiplies each element to its counterpart same index
9. dividing arrays together cannot be done with lists
    x =np.array([3, 8, 15])
    y =np.array([1, 2, 3])
    z = x / y  # z is now np.array([3., 4., 5.]) divides elements in first array to its counterpart same index in other array (produces float)
10. subtracting arrays together cannot be done with lists
    x =np.array([3, 8, 15])
    y =np.array([1, 2, 3])
    z = x - y  # z is now np.array([2, 6, 12]) subtracts counterpart same index element from first array element
12. concatenate arrays (np.concatenate) forces organization to append arrays instead of adding each element
    x =np.array([3, 9, 18])
    y =np.array([64, 7, 12])
    z = np.concatenate([x, y])  # z is now [3, 9, 18, 64, 7, 12]
14. == with arrays

```python3
     import numpy as np

    
    a = 5
    b = 6
    print(a == b)
    
    a = 5
    b = 5
    print(a == b)
    
    x = [1, 2, 3]
    y = [1, 2, 4]
    print(x == y)
    
    xa = np.array([1, 2, 3])
    ya = np.array([1, 2, 4])
    print(xa == ya)
    areAllEqual = (xa == ya).all()
    print(areAllEqual)
    
    xa = np.array([3, 2, 1])
    ya = np.array([5, 0, 4])
    print(xa > ya)
    
    xa = np.array([4, 3, 1])
    print(xa > 2)
    
    # this will give an error
    # x =np.array([3, 9, 18])
    # y =np.array([64, 7, 12])
    # if x == y:
    #     print("same")
    # else:
    #     print("different")
```
