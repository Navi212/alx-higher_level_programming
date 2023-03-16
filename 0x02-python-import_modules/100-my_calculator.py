#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv_len = len(sys.argv) - 1

    if (argv_len != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    op = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = op[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
