#!/bin/bash

echo "enter file name"
read name
if [ -f $name ]
then 
echo "give persmission to file "
sudo chmod 644 $name
echo "permission granted"
ls -l $name
elif [ -d  $name ]
then	
echo "give persmission to directory "
sudo chmod 755 $name
ls -ld $name
echo "permission granted"
else 
echo "file/dir doesnot exist"	
thanks
fi

