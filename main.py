#!/usr/bin/env python3

import clientA, clientB, clientC, clientD, clientE
import server
import time
import threading
import sys
import server

def main_thread():
    server.thread_start()
    time.sleep(1)
    clientA.thread_start()
    clientB.thread_start()
    clientC.thread_start()
    clientD.thread_start()
    clientE.thread_start()

if __name__ == '__main__':
    t = threading.Thread(target = main_thread,args=())
    t.setDaemon(True)
    t.start()
    while True:
        c = sys.stdin.read(1)
        if c == 'q':
            sys.exit()

