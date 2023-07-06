import threading
import time
Lock1 = threading.Lock()
Lock2 = threading.Lock()

def t1():
    Lock1.acquire(timeout=1) #timeout用於處理deadlock
    time.sleep(0.001)
    Lock2.acquire(timeout=1)
    for i in range(5):
        print(str(i)+"s")
        time.sleep(1)
    print("end 1s thread")
    Lock1.release()
    Lock2.release()

def t2():
    Lock2.acquire(timeout=1)
    time.sleep(0.001)
    Lock1.acquire(timeout=1)
    for i in range(10):
        print("500ms")
        time.sleep(0.5)
    print("end 500ms thread")
    Lock1.release()
    Lock2.release()

firstThread = threading.Thread(target = t1)
secondThread = threading.Thread(target = t2)
firstThread.start()
secondThread.start()
firstThread.join()
secondThread.join()
print("finish all")