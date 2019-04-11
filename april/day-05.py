'''
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 
decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

Monte Carlo methods rely on random sampling. In this case, if we take a cartesian plane and inscribe a circle with radius r inside a square with lengths 2r, then the area of the circle will be πr2 while the area of the square will be (2r)2 = 4r2. Then, the ratio of the areas of the circle to the square is π / 4.

'''

import threading
from random import uniform
from math import pow


def generate():
    return (uniform(-1, 1), uniform(-1, 1))


def is_in_circle(coords):
    return pow(coords[0], 2) + pow(coords[1], 2) < 1


def estimate():
    iterations = 10000000
    in_circle = 0

    for _ in range(iterations):
        if is_in_circle(generate()):
            in_circle += 1

    pi_over_four = in_circle / iterations

    return pi_over_four * 4


class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print("Starting " + self.name)
        d = estimate()
        print(self.name + " ended: " + str(d) + "\n")


t1 = myThread(1, 't1')
t2 = myThread(2, 't2')
t3 = myThread(3, 't3')

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

print("Done")
