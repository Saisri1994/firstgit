#!/usr/bin/python
import os
exitcode=os.system("cat /etc/redhat_release")
if exitcode == 0 :
  print ("sys is redhat")
  packlist=['httpd','mysql']
  servlist=['httpd','mysql']
  for list1 in packlist:
    os.system("sudo yum install %s"%list1)
    for list1 in servlist
      os.system("sudo service list1 start")
      os.system("sudo chkconfig list1 on")
else:
  print("sys is not redhat")
  packdeblist=['apache2','mysql-server']
  serdlist=['apache2','mysqld']
  for list2 in packdeblist:
    os.system("sudo apt install %s" %list2)
      for list2 in serdlist
      os.system("systemctl %s start" %serdlist)
      print "successfully installed"
print "thanks"
