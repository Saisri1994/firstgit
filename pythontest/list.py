#!/usr/bin/python
list=['sai',10,'devops','c','lang','java',448,560,'php',449]
list.append('ss')
print list
list.insert(2,'kum')
print list
del list[4]
print list
print list[1:6]
print list[2:7]
list[list.index('java')]='devops'
print list








