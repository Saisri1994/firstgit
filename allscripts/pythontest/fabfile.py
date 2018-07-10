from fabric.api import *
env.hosts=['192.168.1.108']
env.user='vagrant'
env.password='vagrant'
def jenkins():
  sudo("sudo apt update")
  sudo("apt-get install openjdk-8-jdk -y")
  sudo("wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -")
  sudo("echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list")
  sudo("apt-get update")
  sudo("apt-get install jenkins -y")
  sudo("systemctl start jenkins")
def nexus():
 # run("sudo -i")
  sudo("apt install openjdk-8-jdk -y")
  sudo("export RUN_AS_USER=root")
  sudo("wget http://www.sonatype.org/downloads/nexus-latest-bundle.tar.gz")
  sudo("cp nexus-latest-bundle.tar.gz /usr/local")
  with cd("/usr/local"):
    sudo("tar xvzf nexus-latest-bundle.tar.gz")
    sudo("ln -s nexus-latest-bundle.tar.gz nexusnew")
    sudo("/usr/local/nexusnews/bin/nexusstart")
    sudo("apt install nexus -y")
    sudo("service ufw stop")
def nxos():
  exitcode=('cat lsb_release -a')
  if [exitcode == 0]:
    sudo("apt install nginx -y")
  else:
    sudo("yum install nginx -y")
