# Distinct Colors for 2 types of Comments in VS Code
In June 2023, the MS Visual Studio Code (VS Code) program stopping using a distinct color for comments created with tripple quotoes ("""comment"""  and '''comment'''), also called "docstrings".  The docstrings became colored like comments that are initiated with a pound symbol "#".  Some of us found it annoying that VS Code would assign the same color to both types of comments. This page gives a solution.  It must be applied within each user-account of each computer where you use VS Code.

- https://stackoverflow.com/questions/76436694/in-vs-code-1-79-python-docstrings-are-colored-like-comments-how-do-i-return-it/76440715#76440715
- https://github.com/microsoft/vscode/issues/184836
- https://github.com/microsoft/vscode/pull/182162
  - This one has a solution from github user "k98kurz", posted June 2023 (direct link is:  https://github.com/microsoft/vscode/pull/182162#issuecomment-1583819945).

## A Solution 
Here is how to make the change:
(based on idea from github user "k98kurz", linked above)

- Open and work inside the M.S. Visual Studio Code program.
- Open the "settings.json" file:
  - From "View" menue, select "Command Pallet".
  - In the search box that opens, type "settings json", and
  - select "Preferences: Open user settings (JSON)".  The file will open in a editor window/tab. 
- The  "settings.json" file contains a json dictionary similar to a python-style dictionary.         The file may initially contain something like this:
  
```
 {
    "window.zoomLevel": 3
 }
```
  That example has one dictionary entry.
  
- Inside the curley brackets, ensure the last line of text ends with a comma.  If not, add a comma, which will allow a subsequent dictionary entry to be added.
  E.g., The example becomes: `"window.zoomLevel": 3,`
- Add a new line inside the curley brackets after final (or only) existing entry.
- Then paste the following (reformated from the above-mentioned link)

```
    "editor.tokenColorCustomizations":
      {  "[*]": 
          {"textMateRules":
            [   {   "name": "Docstrings",
                    "scope": "string.quoted.docstring",
                    "settings":
                    {    "foreground": "#CE9178"
                    }
                }
            ]
          }
      },
``` 
NOTE: The comma after the final closing-curley bracket of this dictionary entry is included to prepare for adding subsequent dictionary entries in the future.

### The end result:

Your "settings.json" file may look like this when you are done:

```
{
    "window.zoomLevel": 4,

    "editor.tokenColorCustomizations":
      {  "[*]": 
          {"textMateRules":
            [   {   "name": "Docstrings",
                    "scope": "string.quoted.docstring",
                    "settings":
                    {    "foreground": "#CE9178"
                    }
                }
            ]
          }
      },
}
```
Despite its complication, this examples file has only 2 dictionary entries
