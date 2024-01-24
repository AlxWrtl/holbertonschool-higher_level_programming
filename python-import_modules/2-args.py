#!/usr/bin/python3
import sys

argv = sys.argv[1:]
arg = len(argv)

if arg == 0:
    print(f"{arg} arguments.")

elif arg == 1:
    print(f"{arg} argument:")
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")

else:
    print(f"{arg} arguments:")
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
