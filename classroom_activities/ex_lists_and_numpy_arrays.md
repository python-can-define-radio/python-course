Below, you'll find misc examples demonstrating assignment operators used with "normal" Python lists and numpy arrays.

```python3
import numpy as np



x = [10, 20, 30, 40, 50]
## Assign to the same size slice (replace 3 numbers with 3 numbers)
x[0:3] = [6, 7, 8]
print(x)

## Assign to different size slice (replace 2 numbers with 3 numbers)
y = [10, 20, 30, 40, 50]
y[0:2] = [6, 7, 8]
print(y)

## Another diff-size slice
z = [10, 20, 30, 40, 50]
z[0:3] = [6, 7]
print(y)



#########
## now, compare to numpy
#########

x = np.array([10, 20, 30, 40, 50])
x[0:3] = [6, 7, 8]
print(x)

# Notice that different sizes are not allowed in numpy.
# This is reasonable, as numpy is designed for speedy operations,
# and changing the size most likely requires more 
# resources to shift everything forward or backward
# in memory.
y = np.array([10, 20, 30, 40, 50])
y[0:2] = [6, 7, 8]
print(y)
```
