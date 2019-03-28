appLocation = "/app/was_scripts/iMobileCUG/CUG_Binaries/IMobilemeap_test_CUG.war"
appInstallName = "IMobilemeap_test_CUG"
moduleName = "IMobileMeap"
appInstallURI = "IMobilemeap_test_CUG.war,WEB-INF/web.xml"
targetServer = "WebSphere:cell=IHYDIBMP8-13-CL3Cell03,node=IHYDIBMP8-13-CL3Node03,server=wlimbmem02,cluster=WLIMBCUGCluster02"
appStopName = "IMobilemeapPreprodWL62_27032019.war169be78461d"
appStopURI = "IMobilemeapPreprodWL62_27032019.war,WEB-INF/web.xml"
ctxRoot = "/IMobilemeap_cug_test_old"
virtualHost = "default_host"
libName = "axis_jars"

#App Install, context path and module mapping step
AdminApp.install(appLocation, ['-appname',appInstallName,'-defaultbinding.virtual.host',virtualHost,'-usedefaultbindings','-contextroot',ctxRoot,'-MapModulesToServers',[[moduleName,appInstallURI,targetServer]]])
AdminConfig.save()

#Shared Lib and Parent last association
libr = AdminConfig.getid('/Library:'+libName+'/')
print(libr)
deployment = AdminConfig.getid('/Deployment:'+appInstallName+'/')
print(deployment)
appDeploy = AdminConfig.showAttribute(deployment, 'deployedObject')
print(appDeploy)
clsLoader = AdminConfig.showAttribute(appDeploy, 'classloader')
print(clsLoader)
associate = AdminConfig.create('LibraryRef', clsLoader, [['libraryName', libName]])
print(associate)
pl = AdminConfig.modify(clsLoader, [['mode', 'PARENT_LAST']])
print(pl)
AdminConfig.save()
AdminConfig.showall(clsLoader)

#Stopping the app & modifying the context path
appmanager = AdminControl.queryNames('cell=IHYDIBMP8-13-CL3Cell03,node=IHYDIBMP8-13-CL3Node03,type=ApplicationManager,*')
AdminControl.invoke(appmanager, 'stopApplication', appStopName)
AdminApp.edit(appStopName, ['-CtxRootForWebMod', [[moduleName, appStopURI, "/IMobilemeap_cug_test_old_old"]]])
AdminConfig.save()
AdminNodeManagement.syncActiveNodes()

#Disabling auto restart of stopped binary
deployment = AdminConfig.getid('/Deployment:'+appStopName+'/')
print(deployment)
deploymentsObj = AdminConfig.showAttribute(deployment, 'deployedObject')
tMap = AdminConfig.showAttribute(deploymentsObj, 'targetMappings')
tMap = tMap[1:len(tMap)-1].split(" ")
print(tMap)
for targetMapping in tMap:
    AdminConfig.modify(targetMapping, [["enable", "false"]])
AdminConfig.save()
AdminNodeManagement.syncActiveNodes()

#Starting the application
appManager = AdminControl.queryNames('cell=IHYDIBMP8-13-CL3Cell03,node=IHYDIBMP8-13-CL3Node03,type=ApplicationManager,*')
print(appManager)
AdminControl.invoke(appManager, 'startApplication', appInstallName)
result = AdminApp.isAppReady(appInstallName)
while(result == "false"):
    time.sleep(5)
    result = AdminApp.isAppReady(appInstallName)
print("The application has started...")
appStatus = AdminApp.getDeployStatus(appInstallName)
print(appStatus)
