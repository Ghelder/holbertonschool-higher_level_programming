#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    if (len(argv) - 1) == 0:
        print("0 arguments.")
    elif (len(argv) - 1) == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(len(argv) - 1))
        for i in range(len(argv) - 1):
            print("{}: {}".format(i + 1, argv[i + 1]))
