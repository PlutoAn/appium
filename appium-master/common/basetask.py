# -*- coding: utf-8 -*- 
import unittest
import time
import HTMLTestRunner
import sendMail
import os

from common.sendMail import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class BaseTask(object):
    task = []

    def setTask(self, task):
        self.task = task

    def getTask(self):
        return self.task
    
    def runTask(self, type = 'text'):

        print('show task:%s'%(self.task))

        if len(self.task) == 0:
            print ('task is empty')

        suite = unittest.TestSuite()
        suite.addTests(self.task)

        if type == 'text' or type == '':
            print ('run test')
            
            # 定义报告存放路径
            # filename = '../report/' + timestr + 'TestResult.html' 
            filename = '../report/' 

            if not(os.path.exists(PATH(filename))):
                os.mkdir(PATH(filename))

            filename = '../report/' + 'TestResult.html'
            fp=open(PATH(filename),'wd')

            # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
            runner = HTMLTestRunner.HTMLTestRunner(
                    stream=fp, 
                    title='Qing Ting FM Automation Test Report', 
                    description='The detail of test result:')
            result = runner.run(suite)
            fp.close()

            if len(result.errors) > 0:
                sendMail.send_mail("Test errors", 'Result:%s'%(result))
            elif len(result.failures) > 0:
                sendMail.send_mail("Test failures", 'Result:%s'%(result))
            else:
                sendMail.send_mail("Test success", 'Result:%s'%(result))
   
if __name__ == '__main__':
    task = BaseTask()
    task.runTask()

