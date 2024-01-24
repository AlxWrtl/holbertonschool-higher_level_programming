#!/usr/bin/python3
for numb in range(0, 100):
        if numb // 10 < numb % 10:
            print("{:02d}".format(numb), end=", " if numb != 99 else "\n")
