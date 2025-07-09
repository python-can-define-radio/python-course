from rich import print
from rich.console import Console
import time
import random

console = Console()


def exit():
    print("Thank you for playing.")
    return True


def status(lightyears, air_scrubbers, gorn, fuel, carbon_dioxide):
    console.clear()
    print(f"Lightyears traveled: {lightyears}")
    print(f"You have {air_scrubbers} air_scrubbers left in your canteen.")
    print(f"You have {fuel} fuel.")
    print(f"You have {carbon_dioxide} carbon_dioxide.")
    print(f"The gorn are {abs(gorn)} lightyears behind you.")
    print()


def refuel(gorn, fuel):
    console.clear()
    fuel = 0
    refueling = ["Your scanners detect a vein of crystallized zorpathite embedded in an asteroid that allow you to refuel.", "Drifting near a gas giants rings you pass through a vapor-rich field of myronex plasma allowing your fuel cells to recharge.", "You found a cloud of calcified borauntium and are able to collect enough to refuel, it turns out the ore contains microscopic void-beings that willingly give up their essence to provide thrust. It's ethical, mostly. They 'want' to help, probably.", "Your shuttle touches down on a moon streaked with ferrolune dust, a quick harvest restores your fuel reserves. The dusts molecular spin creates a harmonic resonance within your shuttles reactor, essentially 'singing' energy to your shipe"
    ". It's like jazz.", "You intercept a rogue comet trailing frozen shards of xenthium ore, your shuttles automated refinery kicks in allowing you to refuel.", "Your sensors reveal a subspace pocket brimming with liquid quazaranite, the liquid releases energy by rewinding time in a localized micro-pocket giving your shuttle energy that it 'already used' essentially allowing you to use yesterdays fuel."]
    print(random.choice(refueling))
    gained = random.randint(7, 14)
    gorn += gained
    print(f"The gorn have gained {gained} lightyears on you.")
    return gorn, fuel


def ahead_full(lightyears, carbon_dioxide, fuel, gorn):
    console.clear()
    traveled = random.randint(10,20)
    lightyears += traveled
    carbon_dioxide += 1
    fuel_used = random.randint(1,3)
    fuel += fuel_used
    gained = random.randint(7, 14)
    gorn += gained - traveled
    print(f"You have traveled {traveled} lightyears.")
    print(f"You have used {fuel_used} fuel used total is now {fuel}.")
    print(f"You have gained 1 carbon_dioxide total is now {carbon_dioxide}.")
    print(f"The gorn have traveled {gained} lightyears.")
    return lightyears, carbon_dioxide, fuel, gorn


def ahead_half(lightyears, carbon_dioxide, fuel, gorn):
    console.clear()
    traveled = random.randint(5,12)
    lightyears += traveled
    carbon_dioxide += 1
    fuel += 1
    gained = random.randint(7, 14)
    gorn += gained - traveled
    print(f"You have traveled {traveled} lightyears.")
    print(f"You have used 1 fuel used total is now {fuel}.")
    print(f"You have gained 1 carbon_dioxide total is now {carbon_dioxide}.")
    print(f"The gorn have traveled {gained} lightyears.")
    return lightyears, carbon_dioxide, fuel, gorn


def drink(air_scrubbers, carbon_dioxide):
    if air_scrubbers > 0:
        air_scrubbers -= 1
        carbon_dioxide = 0
        print("The air is breathable again.")
    else:
        print("You have no more air_scrubbers available.")
    return air_scrubbers, carbon_dioxide


def main():
    lightyears = 0
    carbon_dioxide = 0
    fuel = 0
    gorn = -20
    air_scrubbers = 3
    done = False

    console.clear()
    print("[green]Welcome to Space Trek![/]")
    print()
    print("[blue underline]You have stolen a shuttle to make your way across the great Mobian Nebula.[/]")
    print("[blue underline]The gorn want their shuttle back and are chasing you down! Survive your[/]")
    print("[blue underline]space trek and outrun the gorn.[/]")
    print()

    while not done:
        print("""[red on white]A. Replace the air scrubber.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and refuel.
E. Status check.
Q. Quit.[/]""")
        
        choice = input("Choice? ----> ")

        if choice.lower() == "q":
            done = exit()
        elif choice.lower() == "e":
            status(lightyears, air_scrubbers, gorn, fuel, carbon_dioxide)
        elif choice.lower() == "d":
            gorn, fuel = refuel(gorn, fuel)
        elif choice.lower() == "c":
            lightyears, carbon_dioxide, fuel, gorn = ahead_full(lightyears, carbon_dioxide, fuel, gorn)
        elif choice.lower() == "b":
            lightyears, carbon_dioxide, fuel, gorn = ahead_half(lightyears, carbon_dioxide, fuel, gorn)
        elif choice.lower() == "a":
            air_scrubbers, carbon_dioxide = drink(air_scrubbers, carbon_dioxide)
        if 4 <= carbon_dioxide <= 6:
            print("You are running out of oxygen.")
        if carbon_dioxide > 6:
            print("You have died of asphyxiation.")
            done = True
        if fuel > 5 and not done:
            print("Your shuttle is running out of fuel.")
        if fuel >  8 and not done:
            print("Your shuttle is out of fuel.")
            done = True
        if 0 < gorn < 15:
            print("The gorn are getting close.")
        elif gorn >= 0 and not done:
            print("You have been captured by the gorn.")
            done = True
        if lightyears >= 200 and not done:
            print("Congratulations, you have made it across the desert.")
            done = True

main()
