for numb1 in range(0, 10):
    for numb2 in range(numb1 + 1, 10):
        if numb1 == 8 and numb2 == 9:
            print("%02d" % (numb1 * 10 + numb2))
        else:
            print("%02d, " % (numb1 * 10 + numb2), end="")
