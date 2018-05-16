#!/bin/bash


SYS= `free -m| grep Mem | awk '{print $2}'`

echo $SYS

USE= "$(df -h| grep /dev/sda1 | awk '{print $5}')"

UT= "$(uptime | cut -d "," -f2)"

#echo "print the memory size 1st partition is $SYS"

#echo "display the memory size of 2nd partition"

echo "$UT"

echo "display the user used memory percentage"

echo "$USE"


echo "display number of users"

echo "$UT"

