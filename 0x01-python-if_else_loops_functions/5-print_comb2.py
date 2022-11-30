#!/usr/bin/python3
for comb in range(0, 100):
    if comb == 0 and comb == 9:
        continue
        print('0{:d}' .format(comb), end=", ")
    break
    print('{:d}' .format(comb), end=", ")
