# -*- coding: utf-8 -*-

# 直接gauge的
GAUGE_STAT_LIST = [
    'CLIENTS',
    'AUTHED_CLIENTS',
    'TRIGGERS',
    'WORKERS',
    'IDLE_WORKERS',
    'CLIENT_PENDING_MSGS',
    'WORKER_PENDING_MSGS',
]

# 间隔一段时间，然后调用incr的
INCR_STAT_LIST = [
    'CMD_CLIENT_REQ',
    'CMD_CLIENT_CREATED',
    'CMD_CLIENT_CLOSED',
    'CMD_WRITE_TO_WORKER',
    'CMD_WORKER_ASK_FOR_TASK',
    'CMD_WRITE_TO_CLIENT',
    'CMD_WRITE_TO_USERS',
    'CMD_CLOSE_CLIENT',
    'CMD_CLOSE_USERS',
    'CMD_LOGIN_CLIENT',
    'CMD_LOGOUT_CLIENT',
    'TASK_TIME_10_MS',
    'TASK_TIME_30_MS',
    'TASK_TIME_50_MS',
    'TASK_TIME_100_MS',
    'TASK_TIME_300_MS',
    'TASK_TIME_500_MS',
    'TASK_TIME_1_S',
    'TASK_TIME_3_S',
    'TASK_TIME_5_S',
    'TASK_TIME_10_S',
    'TASK_TIME_MORE',
]
