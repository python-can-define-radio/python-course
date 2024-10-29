#!/bin/bash

filestodelete=(
  "$HOME/Desktop/blah/a"
  "$HOME/Desktop/blah/b"
)

echo "The following files and folders will be deleted. Type 'y' to confirm, or 'Ctrl-C' to exit if you need to save any files before deleting."
echo ""

for todel in ${filestodelete[@]}; do
    echo "$todel"
done

echo ""
echo "Delete? (yN)"
read wantdelete

if [ "$wantdelete" != y ]; then
  echo "Aborting."
  exit
fi

for todel in ${filestodelete[@]}; do
    rm -r --interactive=never "$todel"
done
