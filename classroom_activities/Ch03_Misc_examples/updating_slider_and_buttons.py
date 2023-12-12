from guizero import App, Slider, ButtonGroup, Box, Text



def update_gui():

    if float(choice.value) != state:
        choice.value = state
        message.value = "Frequency chosen by slider"
    
    if slider.value != state:
        slider.value = state
        message.value = "Frequency chosen by radio button"


def when_buttongroup_activated():
    global state
    state = float(choice.value)    
    update_gui()
    


def when_slider_moved():
    global state
    state = float(slider.value)
    update_gui()
    
               
state = 104.3e6
app = App()
box = Box(app, height=50, width="fill", border=True)
message = Text(box, "")
box.bg = "orange"
slider = Slider(app, start=88, end=108, width=400, height=50, command=when_slider_moved)
slider.bg = "green"
slider.text_color = "yellow"
slider.text_size = 16
slider.value = state
choice = ButtonGroup(app, options=[93.0, 103.0, 104.0, 105.0], command=when_buttongroup_activated, selected=state)

app.display()
