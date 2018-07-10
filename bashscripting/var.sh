#!/bin/bash
#PACK=httpd
#SVC=httpd

#echo "the package name is $PACK"


#echo "the service name is $SVC"

echo $0

echo "pass package name and service name seperated by space"

echo "pack name is $1"

echo "serv name is $2"

echo "third argument $3"


echo "number of arguements passed to this script is $#"

echo "printing all the arguements below"

echo $@
