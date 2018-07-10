#!/bin/bash

#program to give execute permission to the files in the directory
cd sai

for files in `ls`
do 
echo "`sudo chmod u+x $files`"
cd sai
echo "`ls -l`"
done


