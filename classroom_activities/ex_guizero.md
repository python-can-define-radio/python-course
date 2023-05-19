
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

Exercise #1:  
First, run this.
```python3
## 1

from guizero import App

app = App(title="My first GUIZERO app")

app.display()
```

Exercise #2:  
Adding text.
  - To add things to your app you will need to use widgets.
  - Use the Text widget to add a message to your app. 
```python3
## 2

from guizero import App, Text

app = App(title="My first GUIZERO app")

# create widgets here
Text(app, text="Welcome to my GUIZERO app!")

app.display()
```

Exercise #3:  
Adding user input.
  - Use the Textbox widget to add user input to your app.
  - Sometimes you will make a widget as a variable if you want to use that information later as you see here with the "name" Textbox. 
```python3
## 3

from guizero import App, Text, TextBox

app = App(title="My first GUIZERO app")

# create widgets here
Text(app, text="Welcome to my GUIZERO app!")
Text(app, text="Enter your name:")
name = TextBox(app)

app.display()
```

Exercise #4:  
Adding parameters.
  - You can add parameters to your app globally or individually to a variable like this.
```python3
## 4

from guizero import App, Text, TextBox

# with added "global" parameters
app = App(title="My first GUIZERO app")
app.text_size = 18
app.text_color = "red"
app.height = 800
app.width = 1000
app.bg = "teal"

# create widgets here
Text(app, text="Welcome to my GUIZERO app!")
Text(app, text="Enter your name:")
# with added "individual" variable parameter
name = TextBox(app)
name.text_color = "green"

app.display()
```

Exercise #5:  
Adding a Pushbutton.
  - Use the Pushbutton widget to make your app do something.
  - The Pushbutton widget uses pre-built functions assigned by the command parameter to make something happen if you are unfamiliar with functions refer back to exercise ex_8a_turtle_and_functions.md
```python3
## 5

from guizero import App, Text, TextBox, PushButton

def change_bg():
    app.bg = "aquamarine"
    app.text_color = "blue"
    Text(app, text="Congratulations you changed the background color and text color when you pushed me.")

app = App(title="My first GUIZERO app")
app.text_size = 18
app.text_color = "red"
app.height = 800
app.width = 1000
app.bg = "teal"

# create widgets here
Text(app, text="Welcome to my GUIZERO app")
sometext = Text(app, text="Enter your name:")
name = TextBox(app)
name.text_color = "green"
button = PushButton(app, text="Press me", command=change_bg)

app.display()

```

<details><summary>For a more advanced example you can expand here and look at the following code which creates an IP Subnet Calculator app.</summary>
  
```python3

from guizero import App, Text, PushButton, Picture, TextBox, Combo, Box
import ipaddress


def calculate():
    global boxContents
    
    try:
        net4 = ipaddress.ip_network(f'{Ip_Address.value}/{cidr.value}')
    except ValueError as e:
        boxContents = [
            Text(box, text=f"ValueError: That is not a valid Network ID"),
            Text(box, text=f"with /{cidr.value} as the Subnet Mask"),
            Text(box, text=f"{e}")
        ]     
        return
    
    hosts = 2**(32-int(cidr.value))
    boxContents = [
        Text(box, f"Your Network ID is {net4[0]}"),
        Text(box, f"Your Broadcast ID is {net4[-1]}"),
        Text(box, f"Your Subnet Mask is {net4.netmask}"),
        Text(box, f"You have {hosts-2} available IP addresses"),
        Text(box, f"Your available host range is:"),
        Text(box, f"{net4[1]} to"),
        Text(box, f"{net4[-2]}"),
        Picture(box, image="graphics/subnet.png", align="bottom", height=75, width=75),
        Box(app, height=20, width="fill"),
        Text(app, text="Happy Networking")
    ]

def reset():
    global boxContents
    for item in boxContents:
        item.destroy()

app = App(title="Subnet Calculator")
app.height = 750
app.width = 1000
app.text_color = "blue"
app.text_size = 18
app.bg = "aquamarine"
Box(app, align="left", height="fill", width=20)
Box(app, align="right", height="fill", width=20)
Box(app, align="top", height=20, width="fill")
Box(app, align="bottom", height=20, width="fill")

welcome = Text(app, text="Welcome to the IP Subnet Calculator app!")
welcome.text_size = 28
Text(app, text="")

Text(app, text="Please type a valid IPv4 network ID in the box below.")
Ip_Address = TextBox(app, width=14)
Ip_Address.bg = "white"
Ip_Address.text_size = 18
Ip_Address.text_color = "red"
Text(app, text="")

Text(app, text="Please choose a CIDR value from the dropdown menu for your subnet.")
cidr = Combo(app, options= list(range(8, 30+1)))
cidr.bg = "white"
cidr.text_size = 18
cidr.text_color = "red"
Text(app, text="")

box = Box(app, width=900, height=400, border=True)
box.bg = "teal"
box.text_size = 22
Box(box, align="left", height="fill", width=20)
Box(box, align="right", height="fill", width=20)
Box(box, align="top", height=20, width="fill")
Box(box, align="bottom", height=20, width="fill")

button1 = PushButton(box, text="Calculate", command=calculate)
button1.text_size = 12
button1.text_color = "orange"
button1.align = "right"
button2 = PushButton(box, text="  Reset  ", command=reset)
button2.text_size = 12
button2.text_color = "orange"
button2.align = "left"


app.display()
  
```
  </details>

  
  

At this point, if you finish before the rest of the class, or if you'd like more practice with guizero you can look at this tutorial:

  - https://lawsie.github.io/guizero/start/
