appObj = AdminApp.list(WebSphere:cell=cell01,node=node01,server=srvmem01).split('\n')
print(appObj)
appObj2=AdminApp.list(WebSphere:cell=cell3,node=node3,server=srvmem02).split('\n')
print(appObj)

def Diff(env1, env2): 
    return (list(set(li1) - set(li2))) 
live = ['ca', 'dev', 'qa', 'env', 'ver', 35, 40] 
li2 = ['qa', 'dev','env'] 
print(Diff(env1, env2)) 
print (env1 == env2)
