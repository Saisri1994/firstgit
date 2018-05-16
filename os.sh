#!/bin/bash

echo `lsb_release -a`
if [ $?==0 ]
then 
echo "then given os is debian"
sudo apt install apache2 -y
sudo systemctl start apache2
else
echo "then given os is redhat"
sudo yum install httpd
sudo service httpd start
fi


