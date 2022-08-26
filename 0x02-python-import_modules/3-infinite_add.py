#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    sum_ = 0
    for num in argv[1:]:
        sum_ += int(num)
    print("{:d}".format(sum_))
