#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    count = len(argv)
    i = 1
    sum_args = 0
    while i <= count:
        sum_args += int(sys.argv[i])
        i += 1
    print("{:d}" .format(sum_args))
