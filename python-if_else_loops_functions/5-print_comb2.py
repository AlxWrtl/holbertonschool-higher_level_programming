#!/usr/bin/python3
for numb in range(0, 100):
    if numb == 99:
        print(f"{numb}")

    else:
        numb = "%02d" % (numb) + ", "
        print(f"{numb}", end="")
