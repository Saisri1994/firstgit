#!/bin/bash

for i in {6..10}
do
 `sudo mkdir -p /home/user$i`
 `sudo useradd -m -d /home/user$i -s /bin/bash user$i`
#echo `sudo useradd $i`
echo
echo "user$i:123" | sudo chpasswd

done
