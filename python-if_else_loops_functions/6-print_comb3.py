#!/usr/bin/python3
for numb1 in range(0, 10):
    for numb2 in range(numb1 + 1, 10):
        if numb1 < 9 or numb2 < 9:
            print("%02d, " % (numb1 * 10 + numb2), end="")
        else:
            print("%02d" % (numb1 * 10 + numb2))
