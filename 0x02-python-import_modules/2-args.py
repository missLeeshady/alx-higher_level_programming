#!/usr/bin/python3
import sys
# number of arguments n
n = len(sys.argv[1:])

if n == 0:
    print(f"{n} arguments.")
elif n == 1:
    print(f"{n} argument:\n{n}: {sys.argv[n]}")
i = 1
while(n >= i):
    print(f"{i} arguments:\n{i}: {sys.argv[i]}")
    i += 1
