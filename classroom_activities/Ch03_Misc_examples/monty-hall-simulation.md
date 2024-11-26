## Monty Hall Simulation

This is a simulation that runs the Monty Hall experiment 100 times using 5 doors (instead of the conventional 3 doors).

For more info about the Monty Hall problem statement, see [here](https://betterexplained.com/articles/understanding-the-monty-hall-problem/).

```python3
from random import sample as rs, randint as ri, choice

def sl(x):  return sorted(list(x))
def rc(x):  return choice(list(x))

def runexp(displaydetails: bool):
    pool = {1, 2, 3, 4, 5}
    win = ri(1, 5)
    plr = ri(1, 5)
    hostrevealoptions = sl(pool - {win, plr})
    choi = sl(rs(hostrevealoptions, 3))
    switched = pool - set(choi) - {plr}
    won_from_switch = switched == {win}
    if displaydetails:
        print(f"""
        win: {win}
        playerchoice: {plr}
        hostrevealoptions: {hostrevealoptions}
        hostrevealchoices: {choi}
        player's new choice: {switched}
        if you switched: {won_from_switch}
        """)
    return won_from_switch

print("Running once:")
runexp(displaydetails=True)

numtimes = 100
print(f"Running {numtimes} times:")
switchwincount = 0
switchlosecount = 0
for unused in range(numtimes):
    if runexp(displaydetails=False):
        switchwincount += 1
    else:
        switchlosecount += 1

print("switchwincount", switchwincount)
print("switchlosecount", switchlosecount)
```
