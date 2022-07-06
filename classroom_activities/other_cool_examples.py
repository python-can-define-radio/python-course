
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
        newname = oldname.replace(".fake", ".awesome")

        # Actually do the rename
        os.rename(oldname, newname)
