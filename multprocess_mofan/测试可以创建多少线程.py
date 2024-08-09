import threading
import time
def delay():
    while True:
        time.sleep(1)
        print(threading.current_thread().name)
for i,thread in enumerate(range(100)) :
    thread = threading.Thread(target=delay,name=('thread'+str(i)),args=())
    thread.setDaemon(True)
    thread.start()

time.sleep(15)
