import time
import os
from threading import Thread

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def installApp():
    os.popen("adb install " + PATH('../config/app_release.apk'))      

def inputEvent():
    time.sleep(5)
    os.popen("adb shell input tap 785 1280")

def install():
    t1 = Thread(target=installApp)
    t2 = Thread(target=inputEvent)
    t1.start()
    t2.start()         

if __name__ == '__main__':
        t1 = Thread(target=installApp)
        t2 = Thread(target=inputEvent)
        t1.start()
        t2.start()