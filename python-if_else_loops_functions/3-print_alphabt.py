#!/usr/bin/python3
for ASCII in range(97, 123):
    if ASCII != ord("e") and ASCII != ord("q"):
        print("{}".format(chr(ASCII)), end="")
