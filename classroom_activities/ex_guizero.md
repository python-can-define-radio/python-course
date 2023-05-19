
The goal of the current lesson is to familiarize new students with the "guizero" module of python.

### Some useful resources:
`(Suggestion: When using a web-link, Right-Click with your mouse and select "open in new tab" or new window and then go to that tab/window.)`
- https://lawsie.github.io/guizero/start/

Notes: 
- In the text below, a pair of pound symbols (##) introduces instructions or a comment for you the student.
- Commands to be entered in VS Code are written without any such prefix.
- You may need to install guizero to begin.
  - pip install guizero (from the terminal) 
- guizero builds from top to bottom.
  - Specific placement is possible using (x,y) coordinates but is beyond the scope of this lesson.

### Exercises

First, run this.
```sh
## 1

from guizero import App

app = App(title="My first GUIZERO app")

app.display()
```

Adding text:
  - To add things to your app you will need to use widgets.
  - Use the Text widget to add a message to your app. 
```sh
## 2

from guizero import App, Text

app = App(title="My first GUIZERO app")

message = Text(app, text="Welcome to my GUIZERO app!")

app.display()
```

Adding a Pushbutton:
  - Use the Pushbutton widget to make your app do something.
  - The Pushbutton widget uses pre-built functions assigned by the command parameter to make something happen if you are unfamiliar with functions refer back to exercise ex_8a_turtle_and_functions.md
```sh
## 3

from guizero import App, Text, PushButton

def change_text():
    mytext.value = "You pressed me!"

app = App(title="My first GUIZERO app")

mytext = Text(app, text="Welcome to my GUIZERO app")

button = PushButton(app, text="Press me", command=change_text)

app.display()

```

At this point, if you finish before the rest of the class, or if you'd like more practice with guizero, start working on one of these tutorials:

  - https://lawsie.github.io/guizero/start/
