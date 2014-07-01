#coding: UTF-8

import sys
import math

pi = math.pi
time = 0

while time != "exit":
    time = input()
    print time
    if time != "exit":
        whole_hours = 24.0
        coordinate = []
        digree = (time / whole_hours) * (2.0 * pi)

        print digree

        x = (math.cos(digree) + 1.0) / 2.0
        y = (math.sin(digree) + 1.0) / 2.0

        coordinate.append(x)
        coordinate.append(y)
        print coordinate
    else:
        break