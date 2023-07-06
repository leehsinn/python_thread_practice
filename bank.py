import threading
import time
global x

x = 10000
atmLock = threading.Lock()
def withdraw():
    global x 
    atmLock.acquire()
    my_money = x
    my_money = my_money - 100
    print("get 100")
    time.sleep(1)
    x = my_money
    atmLock.release()

print(x)
t1 = threading.Thread(target=withdraw)
t2 = threading.Thread(target=withdraw)
t1.start()
t2.start()
t1.join()
t2.join()

print(x)