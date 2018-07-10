#!/usr/bin/python
import os
ss="/home/devops/training/sai"
if os.path.isdir(ss):
  print "directory"
elif os.path.isfile(ss):
  print "file"
else:
  print "does not exist"
