from fabric.api import run, sudo, env, settings, hide, parallel
from fabric.colors import yellow, green
def host_type():
    run('uname -s')
def read_hosts():
    """
    Reads hosts from sys.stdin line by line, expecting one host per line.
    """
    import sys
    env.hosts = [line.strip() for line in sys.stdin.readlines()]
@parallel
def restart_apache():
    sudo('systemctl daemon-reload')
    sudo('systemctl restart httpd')
@parallel
def check_data_filesystem():
    #if '2' in run('df -h |grep data|wc -l'):
	#print green(env.host_string)
    sudo('df -h |grep data')
@parallel
def fix_lib_java():
    sudo('ldconfig -f /etc/ld.so.conf.d/java_jvm.conf')
@parallel
def remove_monit():
    sudo('/bin/rm -rf /etc/monit.d')
@parallel
def fix_zabbix():
    from time import sleep
    sleep_time = 2
    sudo('pkill -9 zabbix_agentd')
    print yellow("{0}: Sleeping for {1} seconds...".format(env.host_string,
                                                           sleep_time))
    sleep(sleep_time)
    if 'CentOS release 6' in run('cat /etc/redhat-release'):
        sudo('/etc/init.d/zabbix-agent stop')
    else:
        sudo('systemctl stop zabbix-agent')
    sudo('rm -rf /etc/zabbix')
    sudo('yum remove zabbix-agent -y')
    sudo('puppet-sync')
@parallel
def get_main_nic():
    with settings(hide('warnings', 'running', 'stdout', 'stderr'),
                  warn_only=True):
        result = sudo('facter main_nic')
        print green(env.host_string) + ": " + yellow(result)
