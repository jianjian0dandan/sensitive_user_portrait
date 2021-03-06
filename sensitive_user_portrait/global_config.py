# -*- coding: utf-8 -*-

import os
from flask import Flask

REDIS_HOST_INFLUENCE = '219.224.134.213'
REDIS_PORT_INFLUENCE = '7370'
REDIS_HOST_IP = '219.224.134.216'
REDIS_PORT_IP = '7370'
REDIS_HOST_ACTIVITY = '219.224.134.211'
REDIS_PORT_ACTIVITY = '7370'
REDIS_HOST_CLUSTER = '219.224.134.216'
REDIS_PORT_CLUSTER = '7370'
REDIS_HOST_RETWEET = '219.224.134.212'
REDIS_PORT_RETWEET = '7370'
REDIS_HOST_COMMENT = '219.224.134.212'
REDIS_PORT_COMMENT = '7370'
UNAME2UID_HOST = '219.224.134.211'
UNAME2UID_PORT = '7381'
UNAME2UID_HASH = 'weibo_user'

REDIS_TEXT_MID_HOST = '219.224.134.212'
REDIS_TEXT_MID_PORT = '7370'

REDIS_HOST = '219.224.134.212'
REDIS_PORT = '7370'####

MONITOR_REDIS_HOST = '219.224.134.212'
MONITOR_REDIS_PORT = '7370'

USER_ES_HOST = '219.224.134.213'
ES_CLUSTER_HOST_FLOW1 = ["219.224.134.213:9200","219.224.134.214:9200"]
ES_CLUSTER_HOST_FLOW2 = ["219.224.134.213:9206","219.224.134.214:9206"]

ZMQ_VENT_PORT_FLOW1 = '7387'
ZMQ_CTRL_VENT_PORT_FLOW1 = '6585'
ZMQ_VENT_HOST_FLOW1 = '219.224.134.213'
ZMQ_CTRL_HOST_FLOW1 = '219.224.134.213'

ZMQ_VENT_PORT_FLOW2 = '7388'
ZMQ_CTRL_VENT_PORT_FLOW2 = '6586'

ZMQ_VENT_PORT_FLOW3 = '7389'
ZMQ_CTRL_VENT_PORT_FLOW3 = '6587'

ZMQ_VENT_PORT_FLOW4 = '7390'
ZMQ_CTRL_VENT_PORT_FLOW4 = '6588'

ZMQ_VENT_PORT_FLOW5 = '7391'
ZMQ_CTRL_VENT_PORT_FLOW5 = '6589'

# csv file path

'''
BIN_FILE_PATH = '/home/ubuntu8/yuankun/data' # '219.224.135.93:/home/ubuntu8/yuankun'
'''
BIN_FILE_PATH = '/home/ubuntu8/data1309/20130901'
WRITTEN_TXT_PATH = '/home/ubuntu8/data1309/txt'
# first part of csv file
FIRST_FILE_PART = 'MB_QL_9_1_NODE'

# sensitive words path
SENSITIVE_WORDS_PATH = '/home/ubuntu8/huxiaoqian/user_portrait/user_portrait/cron/flow4/sensitive_words.txt'

# need three ES identification 
USER_PROFILE_ES_HOST = '219.224.134.213'
USER_PROFILE_ES_PORT = 9206
SENSITIVE_USER_PORTRAIT_ES_HOST = ['219.224.134.213:9206','219.224.134.214:9206']
SENSITIVE_USER_PORTRAIT_ES_PORT = '9206'
FLOW_TEXT_ES_HOST = ['219.224.134.213:9206','219.224.134.214:9206']
FLOW_TEXT_ES_PORT = '9206'


# use to identify the db number of redis-97
R_BEGIN_TIME = '2016-05-08'

# use to recommentation
RECOMMENTATION_FILE_PATH = '/home/ubuntu8/huxiaoqian/user_portrait/recommentaion_file'
RECOMMENTATION_TOPK = 10000

# use to config leveldb
#DEFAULT_LEVELDBPATH = '/home/ubuntu8/huxiaoqian/user_portrait_leveldb'

# use to upload the user list for group task
UPLOAD_FOLDER = '/home/ubuntu8/huxiaoqian/user_portrait/cron/group/upload/'
ALLOWED_EXTENSIONS = set(['txt'])


# all weibo database
WEIBO_API_HOST = ''
WEIBO_API_PORT = ''

