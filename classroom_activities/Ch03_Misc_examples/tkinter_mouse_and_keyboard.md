This is useful if you are making a GUI using tkinter (without turtle) and want to react to keypresses or mouse movements.

Sources:
- https://stackoverflow.com/questions/27215326/tkinter-keypress-and-keyrelease-events
- https://stackoverflow.com/questions/22925599/mouse-position-python-tkinter


Keypress: 

```python3
import tkinter

wn = tkinter.Tk()


def down(e):
    print('Down\n', e.char, '\n', e)

def up(e):
    print('Up\n', e.char, '\n', e)

wn.bind('<KeyPress>', down)
wn.bind('<KeyRelease>', up)

wn.mainloop()
```

Mouse:

```python3
import tkinter as tk
root = tk.Tk()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

root.bind('<Motion>', motion)
root.mainloop()
```
