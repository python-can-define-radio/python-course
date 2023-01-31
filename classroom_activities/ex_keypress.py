## Inspired by https://stackoverflow.com/questions/27215326/tkinter-keypress-and-keyrelease-events

import tkinter

wn = tkinter.Tk()


def down(e):
    print('Down\n', e.char, '\n', e)

def up(e):
    print('Up\n', e.char, '\n', e)

wn.bind('<KeyPress>', down)
wn.bind('<KeyRelease>', up)

wn.mainloop()
