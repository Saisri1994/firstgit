#!/usr/bin/python
"""this script for tuple,mylist,dictory"""
a={'course':'devops','language':'c','lang2':'java','lang3':'php'}
print a['lang3']
b=(123,"c",'java','linux','devops','python',455)
print b[-1]
c=[123,"java","sai","sri","s","ss","sss"]
print c[-2]
print b[3:]
print "c",c[2:5]
d="hello devops"
print d[5:][-1]
e={'course':[123,'java',{'lang':'php'}],'language':'c','lang2':'java','lang3':'php'}

f={'course':[123,'java',{'lang':'php'}],'language':(123,{'name':'ss'},523),'lang2':'java','lang3':'php'}

print f['language'][1]['name']

#i={'course':[123,'java',{'lang':'php'}],'language':'c','lang2':'java','lang3':'php'}

#print e['course']
#print e['course'][-1]
#print e['course'][-1]['lang']
