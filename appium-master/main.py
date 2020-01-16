# -*- coding: utf-8 -*- 
import sys
from task.iosSuiteTask import *
from task.androidSuiteTask import *

def iOSRun():
    print 'iOS Run'
    task = iosSuiteTask()
    task.initTask()
    task.runTask()

def iOSCommitCheck():
    print 'iOS commit'
    task = iosSuiteTask()
    task.initCommitCheckTask()
    task.runTask()

def androidRun():
    print 'android Run'
    task = androidSuiteTask()
    task.initTask()
    task.runTask()

def androidCommitCheck():
    print 'android commit'
    task = androidSuiteTask()
    task.initCommitCheckTask()
    task.runTask()

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) == 2:
        if sys.argv[1] == 'android':
            androidRun()
        elif sys.argv[1] == 'ios':
            iOSRun()
        elif sys.argv[1] == 'ios_commit_check':
            iOSCommitCheck()
        elif sys.argv[1] == 'android_commit_check':
            androidCommitCheck()
        else:
            print 'no task Run'
    else:
        androidRun()