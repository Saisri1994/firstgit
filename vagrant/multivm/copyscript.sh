#!/bin/bash
echo "enter source file path to be copied"
read SRC
if [ -f $SRC ] 
then 
    echo "source file exits,continuing the operations"
else 
    echo "source file missing"
exit 2

fi

echo "enter destination file to be copied"

read DST

if [ -d $DST ]

then 
   echo "destination file exits"
else 
   echo "destination file missing"

exit 3
fi 
for IP in `cat hostIP`
do
scp $SRC vagrant@$IP:$DST
done
