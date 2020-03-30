# Python多线程例子来示例加线程锁
# 1。使用线程定义一个子类。线程类
# 2。实例化子类并触发线程
# 3。在线程的运行方法中实现锁

import threading
import datetime

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self):
        print("\n开始 " + self.name)
        # Acquire lock to synchronize thread
        threadLock.acquire()
        print_date(self.name, self.counter)
        # Release lock for the next thread
        threadLock.release()
        print("退出 " + self.name)


def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print("{}[{}]: {}".format(threadName, counter, datefields[0]))


threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread("线程", 1)
thread2 = myThread("线程", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("\n退出程序!!!")
