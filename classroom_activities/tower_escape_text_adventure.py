import random
import time
import sys
import pydash
from termcolor import cprint
from termcolor import colored


def delay_print(words):
    for l in words:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.01)

def inputFromList(question, allowed_responses):
    
    delay_print(question)
    ans = input().lower()
    
    # Special case: `None` means allow anything
    if allowed_responses == None:
        return ans

    while ans not in allowed_responses:
        delay_print(colored(f"You must say one of these: {allowed_responses}\n", "blue"))
        ans = input().lower()
    
    return ans

def cellAction(answer):
    if answer == "skeleton":
        delay_print("You can only carry one weapon and 1 shield you find a small shield.\n")
        state["location"] = "on_the_wall"
        state["prompt"] = "Would you like to take the small shield? "
        state["allowed_resps"] = ["yes", "no", "inv"]
    elif answer == "bucket":
        delay_print("You find an old moldy lockpick which appears to be made out of a leg bone.\n")
        state["location"] = "in_the_bucket"
        state["prompt"] = "Do you want to take the lock pick? "
        state["allowed_resps"] = ["yes","no", "inv"]
    elif answer == "bunk":
        delay_print("You find a small satchel you might be able to carry things in.\n")
        state["location"] = "under_the_mattress"
        state["prompt"] = "Would you like to take the small satchel? "
        state["allowed_resps"] = ["yes", "no", "inv"]
    elif answer == "locked door" and "bone lockpick" in state["inventory"]:     
        state["location"] = "cell_with_pick"
        state["prompt"] = "Would you like to try and use the lockpick on the door? "
        state["allowed_resps"] = ["yes","no", "inv"]
    elif answer == "locked door" and "bone lockpick" not in state["inventory"]:
        delay_print("I don't think that will work you have no way to open it\n")
        state["location"] = "cell"
        state["prompt"] = "Would you like to try and kick the door down? "
        state["allowed_resps"] = ["yes","no", "inv"]
    elif answer == "exit":
        delay_print("You look around the dark dungeon and see a staircase going up or down and a hall in front of you.\n")
        state["location"] = "on_the_stairs"
        state["prompt"] = "Which way would you like to go? "
        state["allowed_resps"] = ["up","down", "hall", "inv"]

def stairsAction(answer):
    if answer == "up":
        delay_print("After about a hundred stairs and around the corner you come to another locked door at the top of the stairs.\n")
        state["location"] = "up_the_stairs"
        state["prompt"] = "Would you like to try and use the lockpick on the door or go back down the stairs? "
        state["allowed_resps"] = ["yes","no", "go back down", "inv"]
    if answer == "down":
        delay_print("After descending about 100 stairs around the corner you find another locked door?\n")
        state["location"] = "down_the_stairs"
        state["prompt"] = "Would you like to try your lockpick on this door, continue down the stairs, or go back up? "
        state["allowed_resps"] = ["yes","no", "continue", "go back up", "inv"]
    if answer == "hall":
        delay_print("After about 50 feet the hallway deadends but the wall looks like very shoddy construction\n")
        state["location"] = "in_the_hall"
        state["prompt"] = "Would you like to inspect the wall, or go back? "
        state["allowed_resps"] = ["inspect", "go back", "inv"]
    if answer == "go back down":
        delay_print("You have returned to the cell you were locked in.\n")
        state["location"] = "on_the_stairs"
        state["prompt"] = "Which way would you like to go? "
        state["allowed_resps"] = ["up","down", "go in", "hall", "inv"]
    if answer == "go back up":
        delay_print("You have returned to the cell you were locked in.\n")
        state["location"] = "on_the_stairs"
        state["prompt"] = "Which way would you like to go? "
        state["allowed_resps"] = ["up","down", "go in", "hall", "inv"]
    if answer == "enter":
        state["location"] = "tower_cell"
        delay_print("This cell looks very similar to the one you woke up in with a window and a table.\n")
        state["prompt"] = "Do you want to check the bucket, check the bunk, check the window, check the table or exit? "
        state["allowed_resps"] = ["bucket", "bunk", "table", "window", "exit", "inv"]
    if answer == "go back in":
        delay_print("When you enter the cell you find it is very similar to the one you woke up in\n"
                    "with one exception there is an old man sitting on the bunk\n")
        state["location"] = "lower_cell"
        state["prompt"] = "What would you like to do? "
        state["allowed_resps"] = ["talk", "exit", "inv"]
    if answer == "go in":
        state["location"] = "cell"
        state["prompt"] = "Do you exit, check the bucket, check the skeleton, or check your bunk? "
        state["allowed_resps"] = ["bucket", "skeleton", "bunk", "exit", "inv"]
    if answer == "continue":
        state["location"] = "bottom_of_stairs"
        state["prompt"] = "It appears to be a deadend there is a big steel door which you can tell is barred from the outside.\n"
        "What would you like to do? "
        state["allowed_resps"] = ["go back up", "wait", "inv"]
    if answer == "wait":
        state["location"] = "bottom_of_stairs"
        state["prompt"] = "You wait patiently while staring at the wall. What would you like to do? "
        state["allowed_resps"] = ["go back up", "wait", "inv"]

def towerAction(answer):
    if answer == "yes":
        state["location"] = "tower_cell"
        delay_print("This cell looks very similar to the one you woke up in with a window and a table.\n")
        state["prompt"] = "Do you want to check the bucket, check the bunk, check the window, check the table or exit? "
        state["allowed_resps"] = ["bucket", "bunk", "table", "window", "exit", "inv"]
    if answer == "no":
        state["location"] = "tower_cell"
        state["prompt"] = "Do you want to check the bucket, check the bunk, check the window, check the table or exit? "
        state["allowed_resps"] = ["bucket", "bunk", "table", "window", "exit", "inv"]
    if answer == "bucket":
        delay_print("There appears to be drinkable water in the bucket\n")
        if "flask" in state["inventory"] and "filled flask" not in state["inventory"]:
            state["location"] = "tower_bucket"
            state["prompt"] = "Do you want to fill the flask? "
            state["allowed_resps"] = ["yes","no", "inv"]
    if answer == "table":
        if "flask" not in state["inventory"]:
            delay_print("You find a small resealable flask.\n")
            state["location"] = "on_the_table"
            state["prompt"] = "Do you want to take the flask? "
            state["allowed_resps"] = ["yes","no", "inv"]
        elif "flask" in state["inventory"]:
            delay_print("There is nothing else on the table.\n")
            state["location"] = "tower_cell"
            state["prompt"] = "Do you want to check the bucket, check the bunk, check the window, check the table or exit? "
            state["allowed_resps"] = ["bucket", "table", "bunk", "window", "exit", "inv"]
    if answer == "exit":
        state["location"] = "up_the_stairs"
        state["prompt"] = "Would you like to enter the cell or go back down the stairs? "
        state["allowed_resps"] = ["enter", "go back down", "inv"]
    if answer == "window":
        delay_print("It has a nice view\n")
        state["location"] = "tower_cell"
        state["prompt"] = "Do you want to check the bucket, check the bunk, check the window, check the table or exit? "
        state["allowed_resps"] = ["bucket", "bunk", "table", "window", "exit", "inv"]
        if "rope" in state["inventory"]:
            delay_print(colored("Congratulations you have made it out of the tower.\n", "green"))
            delay_print(colored("Stay tuned for further text adventures.\n", "green"))
            delay_print(colored("Text Adventures was made possible by Michael Hutchings and Jamie O'Meara.\n", "green"))
            sys.exit()
    if answer == "bunk":
        state["location"] = "under_the_bunk"
        state["prompt"] = "Under the bunk you find a bone shiv a simple but effective weapon, would you like to take it? "
        state["allowed_resps"] = ["yes", "no", "inv"]

def lowercellAction(answer):
    if answer == "yes":
        delay_print("When you enter the cell you find it is very similar to the one you woke up in\n"
                    "with one exception there is an old man sitting on the bunk\n")
        state["location"] = "lower_cell"
        state["prompt"] = "What would you like to do? "
        state["allowed_resps"] = ["talk", "ignore", "exit", "inv"]
    if answer == "no":
        delay_print("You stare blankly at the wall\n")
    if answer == "talk":
        state["location"] = "talking"
        state["prompt"] = "old man mutters...I sure am thirsty, Well hello there youngster, what can I do for you? "
        state["allowed_resps"] = ["who are you", "where am i", "ignore", "exit", "search", "inv"]
        if "filled flask" in state["inventory"]:
            state["allowed_resps"].append("offer flask")
    if answer == "ignore":
        if "ignore" not in state["manners"]:
            state["manners"].append("ignore")
            cprint(state["manners"], "red")
        state["location"] = "lower_cell"
        state["prompt"] = "What would you like to do? "
        state["allowed_resps"] = ["talk", "ignore", "exit", "inv"]
    
def hallAction(answer):
    if answer == "yes":
        state["location"] = "behind_the_wall"
        state["prompt"] = "You see a rope lying on the ground would you like to take it? "
        state["allowed_resps"] = ["yes", "no", "exit", "inv"]
    if answer == "go back":
        delay_print("You returned to the stairwell\n")
        state["location"] = "on_the_stairs"
        state["prompt"] = "Which way would you like to go? "
        state["allowed_resps"] = ["up","down", "hall", "inv"]
    if answer == "inspect":
        delay_print("You find a note scratched into the wall that says 'FIND THE MAP'\n")
        if "dungeon map" in state["inventory"]:
            state["location"] = "in_the_hall"
            state["prompt"] = "Upon closer inspection when compared to the map you find a small indentation maybe you can press it? "
            state["allowed_resps"] = ["go back","press", "inv"]
    if answer == "press":
        state["location"] = "in_the_hall"
        state["prompt"] = "When you press the button the wall recedes and the hallway continues, do you want to go in? "
        state["allowed_resps"] = ["yes","no", "go back", "inv"]
    if answer == "exit":
        delay_print("You returned to the stairwell\n")
        state["location"] = "on_the_stairs"
        state["prompt"] = "Which way would you like to go? "
        state["allowed_resps"] = ["up","down", "hall", "inv"]

def oldMan(answer):
    if answer == "who are you":
        state["location"] = "talking"
        state["prompt"] = "I'm George, who are you? "
        state["allowed_resps"] = ["who are you", "where am i", "i don't know", "search", "exit", "inv"]
    if answer == "where am i":
        state["location"] = "talking"
        state["prompt"] = "You are in the Tower Dungeon! Isn't that obvious? "
        state["allowed_resps"] = ["who are you", "where am i", "search", "exit", "inv"]
    if answer == "i don't know":
        state["location"] = "talking"
        state["prompt"] = "I'm sorry to hear that, is there something I can do for you? "
        state["allowed_resps"] = ["who are you", "where am i", "search", "exit", "inv"]
    if answer == "exit":
        state["location"] = "down_the_stairs"
        state["prompt"] = "Would you like to go back in the room, continue down the stairs, or go back up? "
        state["allowed_resps"] = ["go back in", "continue", "go back up", "inv"]
    if answer == "search":
        state["location"] = "talking"
        state["prompt"] = "Whoa, Whoa, Whoa getting a little handsy there aren't ya? "
        state["manners"].append("search")
        cprint(state["manners"], "red")
        state["allowed_resps"] = ["who are you", "where am i", "ignore", "exit", "inv"]
    if answer == "ignore":
        if "ignore" not in state["manners"]:
            state["manners"].append("ignore")
            cprint(state["manners"], "red")
        state["location"] = "lower_cell"
        state["prompt"] = "What would you like to do? "
        state["allowed_resps"] = ["talk", "ignore", "exit", "inv"]
    if answer == "offer flask":
        if "filled flask" in state["inventory"] and "ignore" not in state["manners"]:
            delay_print("Watcha got in that flask youngun?\n")
            delay_print("Oh nevermind I guess even water would be welcome right about now?\n")
            state["location"] = "talking"
            state["prompt"] = "Thanks for the drink and being so polite why dont you take this! "
            state["allowed_resps"] = ["ok", "who are you", "where am i", "ignore", "exit", "search", "inv"]
    if answer == "ok":
        state["inventory"] = pydash.without(state["inventory"], "filled flask")
        state["inventory"].append("dungeon map")
        cprint(f"Inventory:{state['inventory']}", "red")
        state["location"] = "talking"
        state["prompt"] = "Wow I definitely needed that, is there something else I can do for you? "
        state["allowed_resps"] = ["who are you", "where am i", "ignore", "exit", "search", "inv"]

def takeshield(answer):
    if answer == "yes":
        if "small shield" not in state["inventory"]:
            state["inventory"].append("small shield")
            cprint(f"Inventory:{state['inventory']}", "red")
        state["location"] = "cell"
        state["prompt"] = "Do you check the locked door, check the bucket, check the skeleton, or check your bunk? "
        state["allowed_resps"] = ["bucket", "skeleton", "bunk", "locked door", "inv"]
    if answer == "no":
        state["location"] = "cell"
        state["prompt"] = "Do you check the locked door, check the bucket, check the skeleton, or check your bunk? "
        state["allowed_resps"] = ["bucket", "skeleton", "bunk", "locked door", "inv"]

def takesatchel(answer):
    if answer == "yes":
        if "small satchel" not in state["inventory"]:
            state["inventory"].append("small satchel")
            cprint(f"Inventory:{state['inventory']}", "red")
        state["location"] = "cell"
        state["prompt"] = "Do you check the locked door, check the bucket, check the skeleton, or check your bunk? "
        state["allowed_resps"] = ["bucket", "skeleton", "bunk", "locked door", "inv"]
    if answer == "no":
        state["location"] = "cell"
        state["prompt"] = "Do you check the locked door, check the bucket, check the skeleton, or check your bunk? "
        state["allowed_resps"] = ["bucket", "skeleton", "bunk", "locked door", "inv"]

def takelockpick(answer):
    if answer == "yes":
        if "bone lockpick" not in state["inventory"]:
            state["inventory"].append("bone lockpick")
            cprint(f"Inventory:{state['inventory']}", "red")
        state["location"] = "cell"
        state["prompt"] = "Do you check the locked door, check the bucket, check the skeleton, or check your bunk? "
        state["allowed_resps"] = ["bucket", "skeleton", "bunk", "locked door", "inv"]
    if answer == "no":
        state["location"] = "cell"
        state["prompt"] = "Do you check the locked door, check the bucket, check the skeleton, or check your bunk? "
        state["allowed_resps"] = ["bucket", "skeleton", "bunk", "locked door", "inv"]

def takeflask(answer):
    if answer == "yes":
        if "flask" not in state["inventory"]:
            state["inventory"].append("flask")
            cprint(f"Inventory:{state['inventory']}", "red")
        state["location"] = "tower_cell"
        state["prompt"] = "Do you want to check the bucket, check the bunk, check the window, check the table or exit? "
        state["allowed_resps"] = ["bucket", "table", "bunk", "window", "exit", "inv"]
    if answer == "no":
        state["location"] = "tower_cell"
        state["prompt"] = "Do you want to check the bucket, check the bunk, check the window, check the table or exit? "
        state["allowed_resps"] = ["bucket", "table", "bunk", "window", "exit", "inv"]

def fillflask(answer):
    if answer == "yes":
        if "filled flask" not in state["inventory"]:
            state["inventory"].append("filled flask")
            state["inventory"] = pydash.without(state["inventory"], "flask")
            cprint(f"Inventory:{state['inventory']}", "red")
        state["location"] = "tower_cell"
        state["prompt"] = "Do you want to check the bucket, check the bunk, check the window, check the table or exit? "
        state["allowed_resps"] = ["bucket", "table", "bunk", "window", "exit", "inv"]
    if answer == "no":
        state["location"] = "tower_cell"
        state["prompt"] = "Do you want to check the bucket, check the bunk, check the window, check the table or exit? "
        state["allowed_resps"] = ["bucket", "table", "bunk", "window", "exit", "inv"]

def takeshiv(answer):
    if answer == "yes":
        if "bone shiv" not in state["inventory"]:
            state["inventory"].append("bone shiv")
            cprint(f"Inventory:{state['inventory']}", "red")
        state["location"] = "tower_cell"
        state["prompt"] = "Do you want to check the bucket, check the bunk, check the window, check the table or exit? "
        state["allowed_resps"] = ["bucket", "table", "bunk", "window", "exit", "inv"]
    if answer == "no":
        state["location"] = "tower_cell"
        state["prompt"] = "Do you want to check the bucket, check the bunk, check the window, check the table or exit? "
        state["allowed_resps"] = ["bucket", "table", "bunk", "window", "exit", "inv"]

def takerope(answer):
    if answer == "yes":
        if "rope" not in state["inventory"]:
            state["inventory"].append("rope")
            cprint(f"Inventory:{state['inventory']}", "red")
        state["location"] = "in_the_hall"
        state["prompt"] = "You see nothing else in the room all you can do is exit? "
        state["allowed_resps"] = ["exit", "inv"]
    if answer == "no":
        state["location"] = "in_the_hall"
        state["prompt"] = "The door slowly slides shut what would you like to do? "
        state["allowed_resps"] = ["press", "exit", "inv"]

def lockAction(answer):
    if answer == "no":
        delay_print("You stare blankly at the wall.\n")
    elif answer == "yes" and state["location"] == "cell_with_pick":
        delay_print("You are attempting to unlock the door with the bone lockpick.\n")
        dieroll = random.randint(1,20)
        if dieroll >= 12:
            delay_print("You have sucessfully opened the door!\n")
            delay_print("You look around the dark dungeon and see a staircase going up or down and a hall in front of you.\n")
            state["location"] = "on_the_stairs"
            state["prompt"] = "Which way would you like to go? "
            state["allowed_resps"] = ["up","down", "hall", "inv"]
        else:
            delay_print("you fail, but you may try again.\n")
    elif answer == "yes" and state["location"] == "up_the_stairs":
        delay_print("You are attempting to unlock the door with the bone lockpick.\n")
        dieroll = random.randint(1,20)
        if dieroll >= 12:
            delay_print("You have sucessfully opened the door!\n")
            delay_print("It is very dark but you can make out what appears to be another cell, when the door opens\n"
                        "you see dozens of rats that scatter when the light from the hall hits them.\n")
            state["location"] = "tower_cell"
            state["prompt"] = "Would you like to enter the cell? "
            state["allowed_resps"] = ["yes", "no", "inv"]
        else:
            delay_print("you fail, but you may try again.\n")
    elif answer == "yes" and state["location"] == "down_the_stairs":
        delay_print("You are attempting to unlock the door with the bone lockpick.\n")
        dieroll = random.randint(1,20)
        if dieroll >= 12:
            delay_print("You have sucessfully opened the door!\n")
            delay_print("It is very dark but you can make out what appears to be another cell.\n")
            state["location"] = "lower_cell"
            state["prompt"] = "Would you like to enter the cell? "
            state["allowed_resps"] = ["yes", "no", "inv"]
        else:
            delay_print("you fail, but you may try again.\n")

def kickAction(answer):
    if answer == "no":
        state["location"] = "cell"
        state["prompt"] = "Do you check the locked door, check the bucket, check the skeleton, or check your bunk? "
        state["allowed_resps"] = ["bucket", "skeleton", "bunk", "locked door", "inv"]
    elif answer == "yes":
        delay_print("You are attempting to kick the door open.\n")
        dieroll = random.randint(1,25)
        if dieroll >= 24:
            delay_print("Wow your strong, You have sucessfully opened the door!\n")
            delay_print("You look around the dark dungeon and see a staircase going up or down and a hall in front of you.\n")
            state["location"] = "on_the_stairs"
            state["prompt"] = "Which way would you like to go? "
            state["allowed_resps"] = ["up","down", "hall", "inv"]
        else:
            delay_print("you failed, this could take awhile but you may try again if you wish.\n")

def action(answer):
    if answer == "inv":
        cprint(f"Inventory:{state['inventory']}", "red")
    if state["location"] == "cell":
        cellAction(answer)
        kickAction(answer)
    elif state["location"] == "cell_with_pick":
        lockAction(answer)
    elif state["location"] == "on_the_wall":
        takeshield(answer)
    elif state["location"] == "under_the_mattress":
        takesatchel(answer)
    elif state["location"] == "in_the_bucket":
        takelockpick(answer)
    elif state["location"] == "tower_bucket":
        fillflask(answer)
    elif state["location"] == "on_the_stairs":
        stairsAction(answer)
        lockAction(answer)
    elif state["location"] == "tower_cell":
        towerAction(answer)
    elif state["location"] == "lower_cell":
        lowercellAction(answer)
    elif state["location"] == "in_the_hall":
        hallAction(answer)
    elif state["location"] == "up_the_stairs":
        stairsAction(answer)
        lockAction(answer)
    elif state["location"] == "down_the_stairs":
        stairsAction(answer)
        lockAction(answer)
    elif state["location"] == "on_the_table":
        takeflask(answer)
    elif state["location"] == "under_the_bunk":
        takeshiv(answer)
    elif state["location"] == "talking":
        oldMan(answer)
    elif state["location"] == "bottom_of_stairs":
        stairsAction(answer)
    elif state["location"] == "behind_the_wall":
        takerope(answer)
    else:
        raise NotImplementedError() 


state = {
    "location": None,
    "prompt": None,
    "allowed_resps": None,
    "inventory": [],
    "manners": []
}

delay_print(colored("Welcome to the Tower Escape Text Adventure.\n", "green"))
delay_print(colored("You arise in a cell. You feel dizzy and have no recollection of your life before this.\n", "blue"))
delay_print(colored("You look around and see a locked door, a bucket, your bunk, and an old clothed skeleton chained to the wall.\n", "blue"))

state["location"] = "cell"
state["prompt"] = "Do you check the locked door, check the bucket, check the skeleton, or check your bunk? "
state["allowed_resps"] = ["bucket", "skeleton", "bunk", "locked door", "inv"]

# Forever: ask the user for input
while True:
    answer = inputFromList(state["prompt"], state["allowed_resps"])
    action(answer)

# state["inventory"] = pydash.without(state["inventory"], "water")
# cprint(state["inventory"], "red")