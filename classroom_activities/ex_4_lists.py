### Lists are zero-indexed. That means...
thelist = ["water", "chair", "mug", "mouse"]
           # 0      1        2      3 
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
# Try this. Do you expect an error?
print(thelist[-1])

# 4
# Add a few elements to thelist. Then do this again:
print(thelist[-1])


# 5
# Now make it print the second-to-last element of thelist.


# 6
# Try this. It’s a little counterintuitive.
print(thelist[0:3])


# 7
# Try this.
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
# Try this.
letters = ["a", "b", "c", "d", "e"]
letters[0] = "ROCKET"


# 12
# Modify the previous example to replace “b” with “ROCKET” instead of replacing “a”.


# 13
# Modify the previous example to replace the second-to-last element with “ROCKET”.


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


