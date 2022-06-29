# 1
# Try this. 
# It won't display anything to the screen -- rather, it creates a file.
# Try to find the file it created.

f = open("something_very_unique_file.txt", "w")
f.write("Here are some words.")
f.close()



# 2
# Try this.
f = open("something_very_unique_file.txt", "r")
contents = f.read()
print(contents)
f.close()


