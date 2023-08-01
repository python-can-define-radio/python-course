## Lists

Almost any non-trival program will involve working with a collection, such as a list or an array. This exercise set introduces basic list operations.

```python3
### Lists are zero-indexed. That means...
thelist = ["water", "chair", "mug", "mouse"]
#             0        1       2       3 
### Example:
print(thelist[0])    # This will print water
print(thelist[2])    # What will this print?


# 1
# Try this. Do you expect it to print “water” or “chair”?
thelist = ["water", "chair", "mug", "mouse"]
print(thelist[1])


# 2
# Modify the previous example to print the fourth element of the list (“mouse”).


# 3
# The items in a list can be referred to using negative indexes.
thelist = ["water", "chair", "mug", "mouse"]
#            -4       -3      -2      -1
# Try this:
print(thelist[-1])  # This will print "mouse"
print(thelist[-2])  # What will this print?


# 4
# Let's try that with a longer list:
foods = ["Potatoes", "Beef", "Broccoli", "Lemons", "Grapes"]
#            0          1         2          3        4
#           -5         -4        -3         -2       -1
print(foods[1])  # This prints "Donuts"
print(foods[-1])  # This prints "Pizza"


# 5
# Copy and modify the previous example to print the second-to-last element of `foods`.


# 6
# Try this. Which items does it display? 
# Does it include all of the items you expected? 
print(thelist[0:3])
# Counterintuitively, it always omits the last item, so 0:3 actually
# means item 0, item 1, item 2 (not including 3).


# 7
# Try this.
# Notice that it includes item 1 and item 2, but not item 3.
print(thelist[1:3])


# 8
# Modify the previous example to print elements 0,1,2,3. (Hint: it’s not going to be [0:3], but it’s close to that.)


# 9
# Try this.
print(thelist[1:])


# 10
# Modify the previous example to print all but the first two items.
# Pretend you don’t know how long the list is. (You shouldn’t need to.)


# 11
# You can change an item in the list using the following approach.
# How could you verify that the list was changed? (Hint: use print.)
letters = ["a", "b", "c", "d", "e"]
letters[0] = "ROCKET"


# 12
# Modify the previous example to replace "d" with "WAVE".


# 13
# Modify the previous example to use negative indexing.


# 14
# Try this.
name = "Becky"
print(name[0])

# 15
# Modify the previous example to print the “c” of “Becky”.


# 16
# Try this.
names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
print(names[4][3])


# 17
# Modify the previous example to print the last letter of Sarah’s name (using string indexing).


# 18
# Modify the previous example to print the last letter of the last name in the list. Use negative indexing.


# 19
# Try this.
names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
sentence = "Hello to " + names[1] + " and everyone else."
print(sentence)


# 20
# Try this.
names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
print(f"Hello to {names[1]} and everyone else.")


# 21
# Try this.
names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
id_num = 4
print(f"ID: {id_num} Name: {names[id_num]}")


# 22
# Copy and modify the previous example to
# ask the user for a student id, and then
# displays "The student with id number ___ is named ___".


# 23
# You can add an item to the end of a list using append:
names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
print(names)
names.append("Bob")
print(names)


# 24
# Copy and modify the previous example so that it asks the user
# for a new name that you want to add to the end of the list.


# 25
# You can remove items using del:
names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
print(names)
del names[0]
print(names)


# 26
# Copy and modify the previous example so that it asks the user
# for a position (that is, the index) in the list. Remove that item
# from the list using del, and then display the changed list.


# 27 
# A list can be generated using the range() function.
# Try this:
start = 1
stop = 10+1
step = 2
num_list = list(range(start, stop, step))  
  # range parameters: start #, stop#+1, increment (i.e., the "count by" value)
  # Note: Range always omits the final number, so a "+1" has been added 
  # to shown what the actual stopping number will be.  In this example the stop will occur at 10.
print(num_list)


# 28
# Modify the previous example to create a list that includes all numbers  
# between 0 and 30 that are divisible by 3.  
# Note: 0, 1, 2, 4, etc. are not divisible by 3.  Do not include them.

# 29
# Here are some other list-related functions:
mynums = [23, 7, 8, 10]
print(min(mynums))  # The minimum (smallest) value
print(max(mynums))  # The maximum (largest) value
print(len(mynums))  # The length (how many elements are in the list)
```
