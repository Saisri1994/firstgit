#!/usr/bin/python
import os
exitcode=os.system("cat lsb_release -a")
if [exitcode == 0]:
  print ("sys is ubuntu")
  os.system("sudo apt install nginx -y")    
else:
  print("sys is centos")
  os.system("sudo yum install nginx -y")
  
