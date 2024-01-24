#!/usr/bin/python3
import sys

argv = sys.argv[1:]
arg = len(argv)
result = 0

for value in range(0, len(argv)):
    argv[value] = int(argv[value])
    numbers = int(argv[value])
    result += numbers

if result == 0:
    print("0")

else:
    print(result)

