# Marimo

# To start Marimo first go to the website linked below.

make foldr
terminal
`marimo edit`
new nb

NOTE: Change this to use `pip install marimo` and `marimo edit whatever.py`

- First thing you will do is make a folder on your desktop 'name it whatever you want.'
 - then you need to open the terminal  
 - type `pip install marimo`
 - 
# To create your own Notebook
- Marimo will automatically open with a notebook but for you to start your own.
  - First you will click on the 'try our online playground' link below where it tells you 'View on GitHub'  
(it will then open a new tab)  
  - After you will then click new at the top of the screen, then click New Notebook
(This will once more, open a new tab with your own notebook to begin on.)

# How to create and run a cell
-  To begin creating your own work in a cell you will start on line 1.  
 - (this is the first box within your notebook.)  
- You will then type (import marimo as mo)  This will import marimo into your code.  
 -(Hitting enter will go down to line number 2. Marimo is a live update system which means as you type you can get instant gratification when it shows you right then what you fixed.)  
- To run a cell you can try this code.  `print("Hello World!")`  
(When you hit the little play button at the top right hand corner of the cell the output below your code should say Hello world

# Creating a Slider
- Now we want to make a slider  
 - (this will add a slider to the notebook using whatever parameters you have set)
 - use this code `slider = mo.ui.slider(1, 22)`
 - This will add a slider that counts from 1 to 22 and as you move the slider there will be little images that add one each time you move the slider up, or removes one each time you move the slider down.

# Slider.value
- Now we are going to modify how the slider appears to the user using **slider.value**
   
`{">" * slider.value}`

 - You'll notice that this has called the slider which now has the '>' symbol.
 - As we slide the bar between 1 and 22 that many '>' symbols will appear onscreen.

# Radio Buttons
- Let's move from the slider to buttons instead. Using radio buttons, we can give different preset values to the user to
switch between.

`radiobuttons = mo.ui.radio(
    options=["93.9 Bob FM", "99.5 WKXC FM", "88.3 WAFJ FM"], label="Radio Stations"`

- This creates three different buttons that all have predefined labels that correspond to local Augusta Radio stations
- The user can now freely toggle between these stations

# Radio.value

- Let's see what button was selected by the user by using radio.value

`mo.md(f"You chose {radiobuttons.value}")`

- This will tell you the value of the button the user selected.

### Setup

```
pip install marimo
marimo edit myfirstnotebook.py
```

<!--
PapaB (lead)   TS   CM
Rough draft by 9 am Mon & discuss together?
Topics...
- How to create a notebook
- How to create & run a cell
- Demo of slider
- Demo of using slider.value
- Demo of radio buttons
- Demo of using radio.value
- Maybe 5 or so exercises to reinforce understanding
  - Examples:
    - two sliders: one for length of rectangle, one for width. Display area.
    - radio button to choose "small", "med", "large". Display "That would be ____ t-shirts" (25, 50, 100)
    - 
**NEW THINGS** -- by Jan 2, 9 am:
- demonstrate that order of execution is different from normal python
- demonstrate that code runs reactively, perhaps using this example:
```
import turtle
import marimo as mo
x = mo.ui.slider(0, 500, label="X position")
y = mo.ui.slider(0, 500, label="Y position")
x, y
turtle.goto(x.value, y.value)
```
-->

