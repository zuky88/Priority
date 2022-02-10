#!/usr/bin/env python3

import threading
import time
import random
import common

ps = common.Processor()
NAME = 'ClientB'
NUM = 1

def clientMain():
    data = 0
    while True:
        data = int(random.uniform(0,3))
        ps.set2queue(NAME, NUM, data)
        time.sleep(3)

def thread_start():
    t = threading.Thread(target = clientMain,args=())
    t.setDaemon(True)
    t.start()
