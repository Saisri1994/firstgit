#!/bin/bash

echo "enter source file path to be copied"

read SRC

if [ f $SRC ]
then
echo "source file exists"
else 
echo "source file missing"
exit
read DST
if [-d $DST]
echo "destination exist"

else
echo "destination missing"

DST=""

tar -cvzf sai.gz


