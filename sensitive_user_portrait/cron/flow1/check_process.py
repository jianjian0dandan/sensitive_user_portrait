# -*- coding:utf-8 -*-

import subprocess
import sys
import os
import time
import re

def check_zombie(p_name):
    cmd = 'ps -A -ostat,pid,cmd|grep -e "^[Zz]"|grep %s' % p_name
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    if p.wait() == 0:
        val = p.stdout.read()
        print val
        if p_name in val:
            print '%s is a zombie' % p_name
            pattern = re.compile('\d+')
            result = patern.findall(val)
            for item in result:
                kill_cmd = 'kill -9 %s' % item
                k = subprocess.Popen(kill_cmd, shell=True, stdout=subprocess.PIPE)
    else:
        print 'no zombie exist'

def check(p_name):
    cmd = 'ps aux|grep %s|grep -v "grep"' % p_name
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    if p.wait() == 0:
        val = p.stdout.read()
        print val
        if p_name in val:
            print "ok - %s python process is running" % p_name
    else:
        print "no process is running!"
        os.system("python ./%s &" % p_name)

def check_redis(p_name):
    cmd = 'ps -ef|grep %s|grep -v "grep"' % p_name
    restart_cmd = 'cd /home/ubuntu3/huxiaoqian/redis-2.8.13 && src/redis-server redis.conf'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    (stdoutput, erroutput) = p.communicate()
    val = stdoutput
    if p_name in val:
        print "ok - %s process is running" % p_name
    else:
        os.system(restart_cmd)

def check_elasticsearch(p_name):
    cmd = 'ps -ef|grep %s|grep -v "grep"' % p_name
    restart_cmd = 'cd /home/ubuntu3/yuankun/elasticsearch-1.6.0 && bin/elasticsearch -Xmx15g -Xms15g -Des.max-open-files=true -d'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    (stdoutput, erroutput) = p.communicate()
    if p_name in stdoutput:
        print "%s ok - %s process is running" % (time.ctime(), p_name)
    else:
        os.system(restart_cmd)

if __name__ == '__main__':
    '''
    # test procedure running
    d_name = ['redis_to_es.py','zmq_vent_weibo.py', 'zmq_work_weibo.py']
    for item in d_name:
        check(item)

    # test redis running
    check_redis("redis")

    # test elasticsearch running
    check_elasticsearch("elasticsearch")
    sys.exit(0)
    '''
    check_zombie('apt-get')
