'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n,
and calls f after n milliseconds.
'''

import time
import threading


# method 1
class Scheduler:
    def __init__(self):
        pass

    def delay(self, f, n):
        def sleep_then_call(n):
            time.sleep(n / 1000)
            f()

        t = threading.Thread(target=sleep_then_call)
        t.start()


# method 2
def setTimeout(callback, miliseconds):
    now = int(round(time.time() * 1000))
    end = now + miliseconds

    while (now < end):
        now = int(round(time.time() * 1000))

    callback()


# method 3
class Scheduler2:
    def __init__(self):
        self.fns = []  # [callback, due] tuple
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.fns:
                if (now > due):
                    fn()

            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            time.sleep(0.01)

    def delay(self, f, timeout):
        currentTime = time() * 1000
        self.fns.append((f, currentTime + timeout)


def func():
    print("I am called")


sch = Scheduler2()
sch.delay(sch, func, 2000)
