

from fabric.api import * #applicaation programming interface

# uname -r

env.user = 'python'
env.hosts = 'vsftpd'

def check_kernel():
    run('uname -r')

def update_all():
    sudo('yum update -y')

def result():
    sudo('ls -l /var/www/')

def dir_create():
    local('mkdir /tmp/fabricdir')

env.roledefs = {
        'webservers': ['localhost','10.0.0.8']
}

@roles ('webservers')
def check_uptime():
    run('uptime')

def copy():
    put('/etc/hosts','/home/python/hostsfab', mode=777)

def port_number():
    prompt('Which port?', default=80, validate=int)

def reboot():
    reboot(wait=30)

def download():
    get('/etc/passwd','/tmp/passwdvsftpd')
