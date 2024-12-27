# Marimo

# To start Marimo first go to the website linked below.

NOTE: Change this to use `pip install marimo` and `marimo edit whatever.py`

 https://marimo.io/  
 -> This will take you to the website where you will start using Marimo.

# To create your own Notebook
- Marimo will automatically open with a notebook but for you to start your own.
  - First you will click on the 'try our online playground' link below where it tells you 'View on GitHub'  
(it will then open a new tab)  
  - After you will then click new at the top of the screen, then click New Notebook
(This will once more, open a new tab with your own notebook to begin on.)

# How to create and run a cell
--> To begin creating your own work in a cell you will start on line 1.
(this is the first box within your notebook.)
--> You will then type (import marimo as mo)  This will import marimo into your code.
(Hitting enter will go down to line number 2. Marimo is a live update system which means as you type you can get instant gratification when it shows you right then what you fixed.)
--> To run a cell you can try this code.  `print("Hello World!")`
(When you hit the little play button at the top right hand corner of the cell the output below your code should say Hello world

# Setting up the Specan (shows the spectrum analayzer)
--> In the first cell we will type this `from paragradio.v2024_12 import SpecAnSim`
(This imports the spectrum analyzer into Marimo)
--> You can now either hit enter to go to line 2 or at the left side of the cell there is are two plus buttons.  Whichever one you hit will add a new cell either  below or above the one you just did.
--> Next you will type sa = SpecAnSim() 
(This shortens the SpecAnSim, making it easier and quicker to work into our code.)
-->sa.start() is the next line. 
(this opens up the program for us to use.)
[Marimo](https://marimo.io/) is "a reactive notebook for Python". In this lesson, we'll explore how to use it.

# Setting up a Center Frequency
--> We now want to set up a center frequency.  To do that we will use the following code.  * sa.set_center_freq(93.3e6) 
(you will see this when the spectrum analyzer opens, the frequency that it starts on will be 93.3.

# Creating a Slider
--> Now we want to create a slider for our spectrum analyzer.  To do that we will use the following code. fre = mo.ui.slider(93.5e6, 93.8e6),
(this will add a slider to our system with a starting frequency of 93.5e6 and an ending frequency of 93.8e6.

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

