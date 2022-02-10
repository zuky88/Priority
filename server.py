#!/usr/bin/env python3

import threading
import queue
import datetime

q = queue.Queue()

def thread_start():
    t = threading.Thread(target = serverMain, args = (q,))
    t.setDaemon(True)
    t.start()

def serverMain(q:queue.Queue):
    ls = [0] * 5
    while True:
        while not q.empty():
            msg = q.get()
            ls[msg[0]] = msg[1]
            output = 0
            for d in ls:
                if d > 0:
                    output = d
            now = datetime.datetime.now()
            print('[server]List:{0},{1}'.format(ls, now))
            print('[server]Outpit:{0}'.format(output))

def msg_send(msg):
    ls = []
    for i in msg:
        ls.append(i)
    q.put(ls)
