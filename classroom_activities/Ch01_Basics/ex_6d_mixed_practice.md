## Mixed practice

1. Make a word guessing game. The user should be able to continue guessing until guessing the word correctly (regardless of uppercase/lowercase). Every time the user guesses, you should display how many guesses the user has taken so far. Give special messages after certain guesses -- for example, after the third guess, say "Three strikes, you're out! Just kidding, you can keep guessing." _Note: For extra fun, use the Python `termcolor` module._

2. Make a number guessing game. Give the user feedback with each guess: "Too high" or "Too low".

3. Make a data file called `original_names.txt` with the following content:
      ```
      Bob Smith
      Alley Cat
      Mona Jones
      ```
4. Add some more names to the *.txt file.

5. Start a new "*.py" file or use an existing one. Use Python to do the following:
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
