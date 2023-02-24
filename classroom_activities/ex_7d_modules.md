When importing modules, there are a few approaches you can use:

Import the whole module:

```python3
import math
print(math.sqrt(5))
```

Import one function:

```python3
from math import sqrt
print(sqrt(5))
```

Import the whole module, and give it another name ("alias"):

```python3
import math as m
print(m.sqrt(5))
```

Import everything from the module:

```python3
from math import *
print(sqrt(5))
```
