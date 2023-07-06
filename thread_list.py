from time import sleep
import threading

def crawler(page):
    data = [page+1,page+2,page+3]
    ans = []
    for i in data:
        ans.append(i)
        #print("page"+str(page)+", data is"+str(i))
        sleep(1)
    print(page,ans)

allpage = 5
threadList = []

for page in range(allpage):
    t = threading.Thread(target=crawler,args=(page,))
    t.start()
    sleep(1)
    threadList.append(t)



for t in threadList:
    t.join()

print("end")