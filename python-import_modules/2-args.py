#!/usr/bin/python3
import sys

argv = sys.argv[1:]
arg = len(argv)

if arg == 0:
    print(f"{arg} arguments.")

else:
    print(f"{arg} arguments:")
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
