#!/bin/bash

###this is bash script###

#assigning the variables
#VARIABLE=123
#SCRIPT=456
PACKAGE=apache2
SRVNAME=apache2
SRCHTML=index.html
DEST=/var/www/html

# installing the package apache2

echo "install package"
sudo apt install $PACKAGE -y

#checking status

echo "checking status"
sudo systemctl status $PACKAGE

#starting  the sevice

echo "starting service "
sudo systemctl start  $PACKAGE

#deploy html file
echo "copying files"
sudo cp -rfv $SRCHTML $DEST

#restart the service

echo "restart the service"
sudo systemctl restart $PACKAGE

#display the wishes
#echo "GOOD MORNING "

#message content
#echo "hai this is bashscript"

#display the variable value


#echo "assigning the variable $VARIABLE"
#echo "assigning the variable $SCRIPT"
