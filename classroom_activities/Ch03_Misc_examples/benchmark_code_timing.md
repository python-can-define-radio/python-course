# Using the timeit function to test how long your code takes to run.

```python3
from timeit import timeit
## good example of if/if vs if/elif

mycode1 = """
def multipleif(text):
    if text == 'sometext':
        print(text)
    if text == 'nottext':
        print("notanytext")

text = 'sometext'
"""
mycode2 = """
def eliftest(text):
    if text == 'sometext':
        print(text)
    elif text == 'nottext':
        print("notanytext")

text = 'sometext'
"""

print(timeit(stmt=mycode1, number=10000000))


print(timeit(stmt=mycode2, number=10000000))
```
