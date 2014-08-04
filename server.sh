#!/bin/bash
rsync --daemon
/usr/sbin/sshd -D
