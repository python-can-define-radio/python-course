1. Make a data file called `original_names.txt` with the following content:
      ```
      Bob Smith
      Alley Cat
      Mona Jones
      ```
2. Add some more names to the *.txt file.

3. Start a new "*.py" file or use an existing one. Use Python to do the following:
   1. Open the data file and split the lines like so:  
      ```python3
      f = open("original_names.txt", "r")
      lines = f.read().splitlines()
      for line in lines:
          print(line)
      ```
   2. For each name (i.e.: each line of the file):  
        1. If the name contains a space:
           1. Try using `.split()` on the line.  (What does it do?)
           2. Construct an username like so: Bob Smith would be "bsmith" or "smith_b", etc.
           3. Display " ____ 's username is ____ "
        2. If the name does not contain a space:
           1. Display " ____ 's username is ____ " (with the same name in both blanks).
          
