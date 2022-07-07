
#####################
## Example: Batch renaming files

import os

# Fetch a list of files
thefiles = os.listdir(".")

# For each of the files in that list,
for oldname in thefiles:

    print(f"One of the files in here is ... {oldname}")
    
    if oldname.endswith(".fake"):

        # Make a new name
        # (See also note below)
        newname = oldname.replace(".fake", ".awesome")

        # Actually do the rename
        os.rename(oldname, newname)

## Note:
## If the goal is to just change the file extension, then this
## may do more than desired -- if the file were, for example,
## my.fake.file.with.a.long.name.fake
## then both occurences of ".fake" would be replaced,
## rather than just the extension.
## The better (but somewhat more ugly) way would be to do something like this:
## extension = ".fake"
## if oldname.endswith(extension)
##    firstPart = oldname[:-len(extension)]
##    newname = firstPart + ".awesome"
