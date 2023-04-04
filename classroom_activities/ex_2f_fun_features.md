This is an optional exercise that demonstrates some fun features.

## Delay printing

Source: https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line

```python
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

delay_print("hello world")
```

## Color output

First, in a terminal, run this:

```
pip3 install termcolor
```

Then, in Python, run this:

```
from termcolor import cprint

cprint("Hello, World!", "green", "on_red")
```

For more examples, see the termcolor github page: https://github.com/termcolor/termcolor

## Sounds

First, in a terminal, run this:

```
pip3 install playsound
```

Then, in Python, run this:

```
from playsound import playsound

playsound("You_must_pick_a_filename.mp3")
```
