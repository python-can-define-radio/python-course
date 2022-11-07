# How to disable middle click within the Linux operating system

This is useful when your mouse pointing device has a scroll wheel that performs as a middle button.

In the terminal program, type and press enter:

```
xmodmap -e "pointer = 1 25 3 4 5 6 7 8 9 10"
```

This will disable the middle click until you log out.

# How to make the change persistent

We want to put that command in the `.bashrc` file, because that runs on login.

1. Confirm that it isn't already in the file:  
       `grep xmodmap .bashrc`      
2. Make a backup:  
       `cp .bashrc .bashrc_backup` 
3. Confirm backup worked:  
       `diff .bashrc .bashrc_backup` 
4. Append:  
       `echo -e '\n\nxmodmap -e "pointer = 1 25 3 4 5 6 7 8 9 10"'`
5. Confirm change worked:  
       `diff .bashrc .bashrc_backup` 

## To make a script for easy running on multiple occasions:

In the terminal, go to the Desktop:

```
cd ~/Desktop
```

_NOTE: Throughout this document, after each command (e.g. "xmodmap....10", above), press the {Enter} key._

Write the command into a file:

```
echo 'xmodmap -e "pointer = 1 25 3 4 5 6 7 8 9 10"' > disable-middle-click.sh
```

Make that file executable:

```
chmod +x disable-middle-click.sh
```

Now, you may run the file:

```
./disable-middle-click.sh
```

---------------

## To re-enable middle click:

```
xmodmap -e "pointer = 1 2 3 4 5 6 7 8 9 10"
```

When the computer is rebooted, most likely it will revert to a state in which the middle click function of the scroll wheel/middle button is enabled.


