#!/bin/bash

# Transfer a file from local host to scirouter.cslab.ece.ntua.gr.

# Check arguments
if [[ $# != 1 ]] ; then
    echo 'Usage: ./to-remote.sh file_path'
    exit 1
fi

# Move from local to orion
scp -r $1 parlab01@orion.cslab.ece.ntua.gr:~/
# Move from orion to scirouter
scp -r parlab01@orion.cslab.ece.ntua.gr:~/$1 parlab01@scirouter.cslab.ece.ntua.gr:~/

