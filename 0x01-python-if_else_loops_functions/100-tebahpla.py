#!/usr/bin/python3

for i in range(122, 96, -1):
        ch = chr(i)
        if (i % 2 == 1):
                ch = chr(i - (ord('a') - ord('A')))
        print("{}".format(ch), end="")
