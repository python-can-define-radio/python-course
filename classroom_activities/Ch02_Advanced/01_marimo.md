# Marimo

### Setup 

- Make a folder on your desktop. 
- Name it whatever you want without spaces or special characters.
- Open the folder.
- Right click the background of the folder, and click "Open in terminal".
- Type `pip install marimo`.  
- Once it has finished installing you will type `python3 -m marimo edit`. This will open a web browser to the marimo workspace.
- Click "Create a new notebook".
- To save your notebook select the save icon on the bottom right or use ctrl + s.
- Marimo notebooks use the same .py file extension as a regular python file.

### How to run a cell

- Click in the cell {{ TODO screenshot }}.  
- Type `2 + 3`.
- Run the cell by pressing ctrl + enter or by clicking the triangle play button in the top-right corner of the cell.
- Any time you change a cell, you have to re-run that cell for marimo to be aware of the changes. 

### How to create a new cell

To create a new cell, you can do either of these:
- Click one of the two `+` buttons on the left of the cell. (Explore: what's the difference?)
- Alternatively, use shift + enter, which runs your cell and creates a new one.

### Creating a Slider

- Type `import marimo as mo`  This will import marimo into your code.
- Now we want to make a slider with specific parameters 
- use this code `slider = mo.ui.slider(1, 22)` then continue to the next line and type `slider`.  Hit ctrl + enter or click the triangle play button to re-run the cell.
- This will add a slider that shows the range from 1 to 22 and as you move the slider there will be a tooltip that shows you the numbers as you move the slider.

### Using the slider's value

- Now we are going to use `slider.value` to display a character as many times as the slider value.
- In a new cell type: `">" * slider.value`
- You'll notice that this has used the slider value with the '>' symbol.
- As we slide the bar between 1 and 22 that many '>' symbols will appear onscreen.

```
## Exercise 1
## Create an area-of-a-circle calculator.
## Provide a slider for the radius of the circle.
## Display "The area of a circle with a radius of __ is __".

## Exercise 2
## Create an area-of-a-rectangle calculator.
## Provide two sliders for the user, one each for length and width.
## Display "The area of a rectangle with length __ and width __ is __".
```

### Creating Radio Buttons

- We can use a radio button element to give different preset values for the user to switch between.

`radiobuttons = mo.ui.radio(options=["Apple", "Pear", "Banana"], label="Fruits")`

- This creates three different buttons that all have defined labels.
- The user can now freely toggle between these values.

### Using the button's value

- Let's see what button was selected by the user by using the `.value` attribute:

`mo.md(f"You chose {radiobuttons.value}")`

- This will tell you the value of the button the user selected.

Next, we will try a few examples in marimo that can be useful in future projects.

```
## Exercise 2
## Create an radio button element that allows switching between three defined FM channels.
## The three stations should be 96.7, 99.5, and 101.7.
## use the .value attribute to show what the current selection by the user.
```

# Other useful UI elements

### Creating a number input

- Type `num = mo.ui.number(start=0, stop=10, step=2)` to create a number input textbox.
- Type `num` to render the marimo ui element(dropdown box). Run the cell.

### Creating a dropdown box

- Use `dd = mo.ui.dropdown(["A", "B", "C", "D"])` to create a dropdown box.
- Type `dd` to render the new dropdown. Run the cell.

### Creating a calendar

- To create a calender in marimo and select a date use the following:
- Type `mo.ui.date()`. The calendar will render by running the cell with that command only.
- You can interact with it by clicking on the date, and the calendar will open to allow a change.
