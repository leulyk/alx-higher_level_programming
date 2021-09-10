#!/usr/bin/python3

import calculator_1 as calc
from sys import argv, exit

if __name__ == "__main__":
        operators = "+-*/"
        errormsg1 = "Usage: ./100-my_calculator.py <a> <operator> <b>"
        errormsg2 = "Unknown operator. Available operators: +, -, * and /"
        if len(argv) != 4:
                print("{}".format(errormsg1))
                exit(1)
        if argv[2] not in operators:
                print("{}".format(errormsg2))
                exit(1)
        num1 = int(argv[1])
        num2 = int(argv[3])
        if argv[2] == '+':
                print("{} + {} = {}".format(num1, num2, calc.add(num1, num2)))
        if argv[2] == '-':
                print("{} - {} = {}".format(num1, num2, calc.sub(num1, num2)))
        if argv[2] == '*':
                print("{} * {} = {}".format(num1, num2, calc.mul(num1, num2)))
        if argv[2] == '/':
                print("{} / {} = {}".format(num1, num2, calc.div(num1, num2)))
