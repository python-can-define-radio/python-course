import pyautogui
# import time

# def record():
#     f = open("mouseposition.txt", "w")
#     time.sleep(3)
#     for x in range(25):
#         print(f"Recorded position {x+1}")
#         pos = pyautogui.position()
#         abouttowrite = f"{pos.x},{pos.y}\n"
#         print(abouttowrite)
#         f.write(abouttowrite)
#         time.sleep(.5)

# def replay():
#     f = open("mouseposition.txt", "r")
#     contents = f.read().splitlines()
#     while True:
#         for item in contents:
#             x,y = item.split(",")
#             xpos = int(x)
#             ypos = int(y)
#             print(f"The position is {xpos}, {ypos}")
#             pyautogui.moveTo(xpos,ypos)
                    

# operation = int(input("Would you like to record(1) or replay(2)? Enter 1 for record or 2 for replay. "))

# if operation == 1:
#     record()
# elif operation == 2:
#     replay()
