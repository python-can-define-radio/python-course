""" Chp 03 Misc -- 'print_enhancements.py' 
    Sept 7, 2023
Goals: 
    1. To move the print location within a terminal window while running a Pyhton program. E.g., move the print location upwards to a line previoiusly printed and over-type existing text.
    2. To enhance the text appearance, e.g. change text color.

Key py modules: blessed & termcolor

ref.: Documentation, ver. 1.20.0, https://blessed.readthedocs.io/en/1.20.0/location.html, accessed Sept 7, 2023

# You man need to run "pip3 install blessed" in a Terminal window.
Note: As usual, pairs of single and pairs of double quotation marks can be used interchangably.
"""

import blessed
import time 
term = blessed.Terminal()
wait = 0.75  # [sec] a pause time used between some print commands.
print(term.purple("\nUsing the 'blessed' module to change colors and move upward in the terminal window."))  # using double quotation marks
print(term.yellow('1. *****C***'))  #using single quotation marks
print(term.yellow('2. ******D**'))
print(term.yellow('3. *******E*'))
time.sleep(wait)
# Next, move the print location up by 2 lines, to print on line "2." again.
# In this example, the move_up command is in its own print statement, and the string to be printed is on a subsequent line.
print(term.move_up(2), end="")  # The 'end=""' is included to keep the print pointer on the intended line.
print(term.blue+"4. ##B##")  #This text will print over line "2."
# The move_down command makes line 3 visible again.
print(term.move_down(1), end="")
time.sleep(wait)
print(term.orange('5. ********F'))
time.sleep(wait)
# Can join the move_up command in same print statement as the text string:
print(term.move_up(1)+term.blue+"6. ##b##")
time.sleep(wait)




""" An alternative -- the termcolor module """
# It has some features like the 'blessed' module.
# You man need to run "pip3 install termcolor" in a Terminal window.
import termcolor as tc
tc.cprint("\nUsing the 'termcolor' module --- \"Hello, to those who read this!\"", "green", "on_white")
# For more examples, see: https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch01_Basics/ex_2f_fun_features.md 