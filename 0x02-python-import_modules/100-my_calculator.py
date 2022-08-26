#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = ['+', '-', '*', '/']
    for i, operator in enumerate(ops):
        func=[add, sub, mul, div]
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == operator:
            print("{} {} {} = {}".format(a, operator, b, func[i](a,b)))
            break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

