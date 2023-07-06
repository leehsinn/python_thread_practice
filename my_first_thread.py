import threading
import time
global x

def my_job(y):
    global x
    print(y)
    for i in range(5):
        x = 0
        time.sleep(0.5)
        print(x)
        #print("finish thread sleep 0.5")
        '''if i ==2:
            x = 6/0'''
    print("end thread")

firstThread = threading.Thread(target = my_job,args=(40,)) #放變數
x = 1
firstThread.start()

for i in range(3):
    x = 1
    time.sleep(0.5)
    #print("finish main sleep 0.5")

firstThread.join() #thread跟主程式一起跑
print("finish all")