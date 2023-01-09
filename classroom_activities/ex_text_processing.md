Using the `.lower()` function:

```python3
## Good
name = input("What is your name? ").lower()
if name == "bill":
    print("Is that short for William?")
else:
    print("You are not the bill man!")

## Good version 2
name = input("What is your name? ")
if name.lower() == "bill":
    print("Is that short for William?")
else:
    print("You are not the bill man!")


## a simple example using file writing
f = open("somefile.txt", "a")
name = input("What is your name? ")
if name.lower() == "bill":
    print("Is that short for William?")
    print("I'll put that in the database")
    f.write(name)
    f.write(" (a great person)")
    f.write("\n")
else:
    print("You are not the bill man!")
    print("I'll make a note of you anyway.")
    f.write(name)
    f.write(" (not really sure who that is)")
    f.write("\n")
f.close()

```

