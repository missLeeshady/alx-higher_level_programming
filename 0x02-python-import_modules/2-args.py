#!/usr/bin/python3
if __name__ == '__main__':
    import sys
# number of arguments n
    n = len(sys.argv[1:])
    i = 1

    if n == 0:
        print(f"{n} arguments.")
    elif n == 1:
        print(f"{n} argument:\n{n}: {sys.argv[n]}")
    else:
        print(f"{n} arguments:")
    while i <= n:
        print("{:d}: {:s}" .format(i, sys.argv[i]))
        i += 1
