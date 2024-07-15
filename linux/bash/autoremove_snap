#! /bin/bash
# Removes old revisions of snaps in Ubuntu
# DISCLAIMER: CLOSE ALL SNAPS BEFORE RUNNING THIS

set -eu
snap list --all | awk '/disabled/{print $1, $3}' |
    while read snapname revision; do
        snap remove "$snapname" --revision="$revision"
    done

# Create a new directory with your bash scripts, for example: mkdir /home/[USER]/bash_scripts
# Add this directory to the PATH variable by: export PATH=$PATH:home/[USER]/bash_scripts 
# This will allow to execute this scripts and all its companions in the same directory no matter where you are located
# Change your script to executable by: chmod 777 [SCRIPT].sh
