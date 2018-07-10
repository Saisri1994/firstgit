from fabric.api import *
env.hosts=['192.168.0.146']
env.user='vagrant'
env.password='vagrant'
def service():
 sudo("yum install httpd")
 run("wget -O short.zip http://www.templatemo.com/download/templatemo_502_short")
 sudo("yum install unzip")
 run("unzip short.zip")
 run("cd templatemo_502_short")
 run("sudo cp -rvf * /var/www/html")
 run("sudo service iptables stop")
 run("sudo service httpd restart")




