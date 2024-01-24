#!/usr/bin/python3
import sys

argv = sys.argv[1:]
arg = len(argv)

if arg == 0:
    print("{} arguments.".format(arg))

elif arg == 1:
    print("{} argument:".format(arg))
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))

else:
    print("{} arguments:".format(arg))
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
