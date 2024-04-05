Create these two files:

### calculator.py

```python3
y = 5

def square(x):
    return x * x

def cube(x):
    return x * x * x

if __name__ == "__main__":
    print(f"__name__ is {__name__}")
    print("Welcome to the calculator")
    usernum = int(input("Pick a num: "))
    print(f"Squared is {square(usernum)}")
    print(f"Cubed is {cube(usernum)}") 
```

### another_program.py

```python3
from calculator import square

if __name__ == "__main__":
    print("This is something really cool")
    print("It calulates ffts and stuff")
    print("And it also squares numbers.")
    choice = input("Which do you want to do?")
    if choice == "fft":
        print("Not implemented yet.")
    elif choice == "square":
        print("No prob!")
        print("What num?")
        x = int(input())
        print(square(x))
    elif choice == "cube":
        print("Yeah!")
        print("What num?")
        x = int(input())
        print(cube(x))
```

Run both to see how `if __name__ == "__main__":` works.
