#!/usr/bin/env python
#*-* encoding=utf8 *-*

import os
import subprocess
import time
import sys
from pyinotify import WatchManager, Notifier, ProcessEvent, IN_DELETE, IN_CREATE, IN_MODIFY

PORT = "2206"
HOST = "127.0.0.1"

class RsyncCmd:
    def __init__(self):
        self.dst = HOST
        self.port = PORT
        self.cmd = "rsync -arz --delete --timeout=60 --port=%s /data/ soone@%s::data --password-file=/etc/rsyncd.client.pas" % (self.port, self.dst)
        print self.cmd

class EventHandler(ProcessEvent):
    def process_default(self, event):
        if event.name.startswith('.') or event.name.endswith('~') or event.name == '4913':
            pass
        else:
            createRsync = RsyncCmd()
            subprocess.call(createRsync.cmd, shell=True)

def fsMonitor(path="/data"):
    wm = WatchManager()
    mask = IN_DELETE | IN_MODIFY | IN_CREATE
    notifier = Notifier(wm, EventHandler(), read_freq=10)
    notifier.coalesce_events()
    wm.add_watch(path, mask, rec=True, auto_add=True)
    notifier.loop()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "cli arguments error"
        print "Usage python pyrsync.py 192.168.18.188 49153"
    else:
        HOST = sys.argv[1]
        PORT = sys.argv[2]

    fsMonitor()
    print "pyrsync start!"
