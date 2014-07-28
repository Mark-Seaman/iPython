#!/bin/bash
# File list test

rmas /home/seaman/Projects/ipython # Remove autosave files
ls /home/seaman/Projects/ipython /home/seaman/Projects/ipython/* | grep -v 'pyc$\|diff$\|out$\|like$'
