#!/usr/bin/python3
for dig1 in range(0, 8):
    for dig2 in range(dig1+1, 10):
        print("{:d}{:d}".format(dig1, dig2), end=", ")
print("{:d}{:d}".format(dig1 + 1, dig2))
