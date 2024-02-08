# DataClasses

[Rich Presentation for ex5b]()

ℹ️ This material coincides with material from python slideshow D (slides 16-30).

### Exercises
Using Python's dataclasses module -- Grouping related data in a single data structure.

```python3
## 1
## Try this.
from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    age: int
    breed: str
   
d1 = Dog("Tucker", 4, "Cocker Spaniel")
d2 = Dog("Henry", 8, "Bassett Hound")

print(d1.name)


```
