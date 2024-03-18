#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    t = 0
    for j in range(len(sys.argv) - 1):
        t += int(sys.argv[j + 1])
    print("{}".format(t))
