import random
import time
import sys



def delay_print(words):
    for l in words:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)


def inputFromList(question, allowed_responses):
    
    delay_print(question)
    ans = input().lower()
    
    # Special case: `None` means allow anything
    if allowed_responses == None:
        return ans

    while ans not in allowed_responses:
        delay_print(f"You must say one of these: {allowed_responses}\n")
        ans = input().lower()
    
    return ans


def cellAction(answer):
    if answer == "skeleton":
        delay_print("The bones are dry.\n")
    elif answer == "bucket":
        delay_print("You find a lock pick.\n")
        state["location"] = "cell_with_pick"
        state["prompt"] = "Do you attempt to unlock the door? "
        state["allowed_resps"] = ["yes","no"]
    elif answer == "bunk":
        delay_print("You find bed bugs.\n")
    

def lockAction(answer):
    if answer == "no":
        print("You stare blankly at the wall.")
    elif answer == "yes":
        dieroll = random.randint(1,20)
        if dieroll >= 12:
            delay_print("You have sucessfully opened the door!\n")
            delay_print("You look around the dark dungeon and see a staircase going out.\n")
            state["location"] = "outside_of_cell"
            state["prompt"] = "Do you go up the stairs? "
            state["allowed_resps"] = ["yes","no"]
        else:
            delay_print("you fail, but you may try again.\n")


def action(answer):
    if state["location"] == "cell":
        cellAction(answer)
    elif state["location"] == "cell_with_pick":
        lockAction(answer)
    else:
        raise NotImplementedError() 


state = {
    "location": None,
    "prompt": None,
    "allowed_resps": None,
}

delay_print("You arise in a cell. You feel dizzy and have no recollection of your life before this.\n")
delay_print("You look around and see a bucket, your bunk, and an old clothed skeleton.\n")

state["location"] = "cell"
state["prompt"] = "Do you check your bucket, check the skeleton or check your bunk? "
state["allowed_resps"] = ["bucket", "skeleton", "bunk"]

# Forever: ask the user for input
while True:
    answer = inputFromList(state["prompt"], state["allowed_resps"])
    action(answer)
