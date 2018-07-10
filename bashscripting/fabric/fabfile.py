#sample fabric function
from fabric.api import*
def hello():
     print ("hello devops")

def hi(name="world"):
    print "hello ",name
def host():
    local("ls -ltr")
def guest():
    run("mkdir sai")
    run("touch sai/f5")
    run("ls -ltr sai/f5")
def pguest():
    put("fabfile.py","/home/vagrant")
def gguest():
    f=prompt("enter file path to download")
    get(f,".",use_sudo=True)
    

