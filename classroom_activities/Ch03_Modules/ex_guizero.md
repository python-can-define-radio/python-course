
### The guizero module  

The goal of the current lesson is to familiarize new students with the "guizero" module of python.

### Notes: 
- You may need to install guizero to begin.
  - `pip install guizero` (from the terminal) 
- guizero builds from top to bottom and spacing or padding is not built in you may have to get creative.
  - Specific placement is possible using (x,y) grid coordinates but is beyond the scope of this lesson.

### Exercises

<i>Exercise #1:</i>  
First, run this.
```python3
## 1

from guizero import App

app = App(title="My first GUIZERO app")

app.display()
```

<i>Exercise #2:</i>  
Adding text.
  - To add things to your app you will need to use widgets.
  - Use the Text widget to add a message to your app. 
<details><summary>Expand here for code.</summary>

```python3
  
## 2

from guizero import App, Text

app = App(title="My first GUIZERO app")

# create widgets here
Text(app, text="Welcome to my GUIZERO app!")

app.display()
  
```
</details>

<i>Exercise #3:</i>  
Adding user input.
  - Use the Textbox widget to add user input to your app.
  - Sometimes you will make a widget as a variable if you want to use that information later as you see here with the "name" Textbox. 
<details><summary>Expand here for code.</summary>
  
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
</details>

<i>Exercise #4:</i>    
Adding parameters.
  - You can add parameters to your app globally or individually to a variable like this.
<details><summary>Expand here for code.</summary>  
  
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
</details>  

<i>Exercise #5:</i>    
Adding a Pushbutton.
  - Use the Pushbutton widget to make your app do something.
  - The Pushbutton widget uses pre-built functions assigned by the command parameter to make something happen if you are unfamiliar with functions refer back to exercise ex_8a_turtle_and_functions.md
<details><summary>Expand here for code.</summary>  

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
</details>  

### Examples  

<details><summary>For more widget examples you can expand here and look at the following code which uses guizero and the IP address module to create an IP Subnet Calculator app.</summary>

```python3
  
from guizero import App, Text, PushButton, TextBox, Combo, Box
import ipaddress


def calculate():
    global boxContents   
    net4 = ipaddress.ip_network(f'{Ip_Address.value}/{cidr.value}', strict=False)
    boxContents = [
        Text(box, f"Your Network ID is {net4[0]}"),
        Text(box, f"Your Broadcast ID is {net4[-1]}"),
        Text(box, f"Your Subnet Mask is {net4.netmask}"),
        Text(box, f"You have {net4.num_addresses - 2} available IP addresses"),
        Text(box, f"Your available host range is:"),
        Text(box, f"{net4[1]} to"),
        Text(box, f"{net4[-2]}"),
    ]

def reset():
    global boxContents
    for item in boxContents:
        item.destroy()

app = App(title="Subnet Calculator")
app.height = 400
app.width = 600
Box(app, align="top", height=20, width="fill")
welcome = Text(app, text="Welcome to the IP Subnet Calculator")
welcome.text_size = 24
Box(app, height=10, width="fill")
Text(app, text="Please enter a valid IPv4 Network ID in the box below.")
Ip_Address = TextBox(app, width=14)
Box(app, height=10, width="fill")
Text(app, text="Please choose a CIDR value from the dropdown menu for your subnet.")
cidr = Combo(app, options= list(range(8, 30+1)))
Box(app, height=10, width="fill")
box = Box(app, width=550, height=175, border=True)
button1 = PushButton(box, text="Calculate", command=calculate)
button1.align = "left"
button2 = PushButton(box,  text="  Reset  ", command=reset)
button2.align = "right"

app.display() 
  
``` 
</details> 
  
<details><summary>For a more advanced example you can expand here and look at the following code which uses guizero and the IP address module to create an IP Subnet Calculator app with even more widget examples.</summary>
  
```python3

from guizero import App, Text, PushButton, Picture, TextBox, Combo, Box, CheckBox, MenuBar, Window
import ipaddress


def calculate():
    global boxContents
    
    try:
        net4 = ipaddress.ip_network(f'{Ip_Address.value}/{cidr.value}', strict=False)
    except ValueError as e:
        boxContents = [
            Text(box2, text=f"ValueError: That is not a valid Network ID"),
            Text(box2, text=f"with /{cidr.value} as the Subnet Mask"),
            Text(box2, text=f"{e}")
        ]     
        return
    
    hosts = 2**(32-int(cidr.value))
    boxContents = [
        Text(box2, f"Your Network ID is {net4[0]}"),
        Text(box2, f"Your Broadcast ID is {net4[-1]}"),
        Text(box2, f"Your Subnet Mask is {net4.netmask}"),
        Text(box2, f"You have {hosts-2} available IP addresses"),
        Text(box2, f"Your available host range is:"),
        Text(box2, f"{net4[1]} to"),
        Text(box2, f"{net4[-2]}"),
        Picture(box2, image="graphics/subnet.png", align="bottom", height=75, width=75),
        Box(app, height=10, width="fill"),
        Text(app, text="Happy Networking")
    ]
    
def reset():
    global boxContents
    for item in boxContents:
        item.destroy()
     
def ch_message():
    if checkbox.value == 1:
        enterNID.value ="Please enter any Host ID from your subnet in the box below."   
    else:
        enterNID.value ="Please enter a valid IPv4 Network ID in the box below."

def enable_calc():
    IP_Address_Length = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    if len(Ip_Address.value) in IP_Address_Length:
        button1.enable()
        button2.enable()
        cidr_message.show()
        cidr.show()
    else:
        button1.enable()
        button2.enable()
        cidr_message.show()
        cidr.show()

def edit_function():
    print("Edit option")

def popup():
    window = Window(app, height=500, width=500, title="About Me")
    window.bg = "yellow"
    Box(window, height=200, width="fill")
    Text(window, text="I'm me (who else would I be?)")

def readme():
    window = Window(app, height=250, width=600, title="Read Me")
    window.bg = "yellow"
    Text(window, text="The Checkbox is just for show\n"
        "the calculator is fully functional with any IP address\n"
        "regardless of whether you use the checkbox or not\n"
        "1) You must enter an IP Address to begin.\n"
        "2) Then select your 'slash notation' (CIDR).\n"
        "3) Thats the box with the red 8 on it.\n"
        "4) Finally click the calculate button.\n"
        "5) Reset and repeat as needed.")
    Text(window, text="NOTE: If you get an error be sure to hit reset to clear the window")

app = App(title="Subnet Calculator")
app.height = 750
app.width = 1000
app.text_color = "blue"
app.text_size = 15
app.bg = "aquamarine"
Box(app, align="left", height="fill", width=20)
Box(app, align="right", height="fill", width=20)
Box(app, align="top", height=20, width="fill")
Box(app, align="bottom", height=20, width="fill")

menubar = MenuBar(app, toplevel=["File", "Edit", "About"],
                  options=[
                      [ ["Calculate", calculate], ["Reset", reset] ],
                      [ ["Just for looks", edit_function], ["I don't really do anything!", edit_function] ],
                      [ ["About the Author", popup], ["Read me", readme] ]
                  ])

welcome = Text(app, text="Welcome to the IP Subnet Calculator app!")
welcome.text_size = 26

box1 = Box(app, width=900, height=200, border=False)
Box(box1, align="left", height="fill", width=10)
Box(box1, align="right", height="fill", width=10)
Box(box1, align="top", height=10, width="fill")
Box(box1, align="bottom", height=10, width="fill")

enterNID = Text(box1, text="Please enter a valid IPv4 Network ID in the box below.")
Ip_Address = TextBox(box1, width=14, command=enable_calc)
Ip_Address.bg = "white"
Ip_Address.text_color = "red"
checkbox = CheckBox(box1, text="I don't know the Network ID let me use a host address!", command=ch_message)
checkbox.text_size = 10
Box(box1, height=10, width="fill")

cidr_message = Text(box1, text="Please choose a CIDR value from the dropdown menu for your subnet.")
cidr_message.hide()
cidr = Combo(box1, options= list(range(8, 30+1)))
cidr.bg = "white"
cidr.text_color = "red"
cidr.hide()
Text(box1, text="")

box2 = Box(app, width=900, height=400, border=True)
box2.bg = "teal"
box2.text_size = 22
Box(box2, align="left", height="fill", width=10)
Box(box2, align="right", height="fill", width=10)
Box(box2, align="top", height=10, width="fill")
Box(box2, align="bottom", height=10, width="fill")

button1 = PushButton(box2, text="Calculate", command=calculate, enabled=False)
button1.text_size = 12
button1.text_color = "orange"
button1.align = "left"
button1.bg = "green"
button2 = PushButton(box2,  text="  Reset  ", command=reset, enabled=False)
button2.text_size = 12
button2.text_color = "orange"
button2.align = "right"
button2.bg = "green"


app.display()
  
```
  </details>

  

At this point, if you finish before the rest of the class, or if you'd like more practice with guizero you can look at the following tutorial:

### Some useful resources:
`(Suggestion: When using a web-link, Right-Click with your mouse and select "open in new tab" or new window and then go to that tab/window.)`
- https://lawsie.github.io/guizero/start/

### Other notes:

- `xset r $PROPERSETTINGGOESHERE`
- `when_key_*`
