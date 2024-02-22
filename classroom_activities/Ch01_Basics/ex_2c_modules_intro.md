<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2023 Jun 06: ex_7d_modules.md       -- Move & rename to organize the course files.
2024 Feb 05: ex_2f_modules_intro.md -- Present it prior to using modules in other lesssons
2024 Feb 14: ex_2c_modules_intro.md
</pre>
</details>

# Modules

ℹ️ This material coincides with material from python slideshow D (slides 4-15).

In Python, modules are packets of code that enhance the operation of Python.
Modules may include multiple Python functions, each giving a specific functionality.
E.g., the "math" modules includes functions such as "sqrt()" and "cos()" 
Using an "import" command, modules may be added to a program to make the module's functionality available to the program.

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
