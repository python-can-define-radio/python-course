#!/bin/bash

filestodelete=(
  "$HOME/Desktop/blah/a"
  "$HOME/Desktop/blah/b"
)

echo "The following files and folders will be deleted. Type 'Y' to confirm, or 'Ctrl-C' to exit if you need to save any files before deleting."
echo ""

for todel in ${myarr[@]}; do
    echo "$todel"
done

echo ""
echo "Delete? (yN)"
read wantdelete

if [ "$wantdelete" != Y ]; then
  exit
fi

for todel in ${myarr[@]}; do
    rm -rfv "$todel"
done



