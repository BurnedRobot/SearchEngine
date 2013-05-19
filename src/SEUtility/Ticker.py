#! /usr/bin/env python
#-*- encoding:utf-8 -*-

import __init__
import threading,time
import sys
from datetime import datetime

class Ticker(object):

    def __init__(self):
        self.tick = True

    def _run(self):
        while self.tick:
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(1.0)

    def start(self):
        print "Beginning:"
        self._start = datetime.now()
        threading.Thread(target = self._run).start()

    def end(self):
        self.tick = False
        self._end = datetime.now()
        print 
        print "End!"

    def TimeCost(self):
        print "Time cost:",self._end - self._start
