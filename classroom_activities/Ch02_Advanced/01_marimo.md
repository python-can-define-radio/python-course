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

- Click in the cell.
- Type `2 + 3`.
- Run the cell by pressing ctrl + enter or by clicking the triangle play button in the top-right corner of the cell.
- Any time you change a cell, you have to re-run that cell for marimo to be aware of the changes. 

### How to create a new cell

To create a new cell, you can do either of these:
- Click one of the two `+` buttons on the left of the cell. (Explore: what's the difference?)
- Alternatively, use shift + enter, which runs your cell and creates a new one.

### How to create a markdown cell

Once a cell is created you can click on the `⋮⋮` to the right of that cell to open a menu.  
Select "view as markdown".  
Now you can write markdown to add flavor to your app.  
Example:  
`# My App`  
The hashtag makes the following text a header which is large. Add more hashtags to decrease the size.

For more Markdown formatting examples, see [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Naming a cell

To name a cell:
*Note: Due to a bug in marimo, your cursor jumps when certain characters are typed, so it is best to copy/paste the name into the name location.*
- Type the name you want in any cell then Ctrl + c (Copy) or Ctrl + x (Cut) to copy it to the clipboard.
- Right click on the `⋮⋮` icon to the right of the cell, then click in the name box and Ctrl + v or right click and select paste to paste the name.
  
### Creating a Slider

- Type `import marimo as mo`  This will import marimo into your code.
- Now we want to make a slider with specific parameters 
- use this code `slider = mo.ui.slider(1, 22)` then continue to the next line and type `slider`.  Hit ctrl + enter or click the triangle play button to re-run the cell.
- This will add a slider that shows the range from 1 to 22 and as you move the slider there will be a tooltip that shows you the numbers as you move the slider.

### Using the slider's value

- Now we are going to use `slider.value` to display a character as many times as the slider value.
- In a new cell type: `"A" * slider.value`
- You'll notice that as we slide the bar between 1 and 22, the chosen number of `A`s will appear onscreen.

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

```
## Exercise 3
## Create an radio button element that allows switching between three defined FM channels.
## The three stations should be 96.7, 99.5, and 101.7.
## In another cell, display "The station you chose is ___".
```

### Creating a number input

- We can use a number input element to give us a textbox scrollbar which only allows numeric input .
- Type `num = mo.ui.number(start=0, stop=10, step=2)` to create a number input textbox.
- Type `num` to render the marimo ui element(dropdown box). Run the cell.

### Using the number input's value

- Here we are using the value indicated in the `number` textbox.

`f"Your chosen value to the power of 2 is {num.value ** 2}"`

```
## Exercise 4
## Create a number input element for picking a number of cars.
## Display "If you bought ___ cars for $25,000 each, the total would be ___."
```

### Creating a dropdown box

- Use `dd = mo.ui.dropdown({"A": 10, "B": 20, "C": 30, "D": 40})` to create a dropdown box.
- Type `dd` to render the new dropdown. Run the cell.
- In a new cell, type `dd.value` then run the cell.
- Make a selection from the dropdown.

```
## Exercise 5
## Create an dropdown element that selects which type of car you want to buy and its price.
## Create a number input element to select how many of that car you would like to purchase.
## Display "If you bought __ cars for __ each, the total cost would be __".
```

### Creating a calendar

- To create a calendar in marimo and select a date, use the following: `mo.ui.date()`
- You can interact with it by clicking on the date, and the calendar will open to allow a change.

```
## Exercise 6  (optional)
## Display the chosen date from the calendar UI element.
```
