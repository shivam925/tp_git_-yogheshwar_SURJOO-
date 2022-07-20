#!/usr/bin/python3

import sys

def add(a, b):
    sum = a + b
    print(sum)

try: 
    a = int( sys.argv[1] )
    b = int( sys.argv[2] )
except IndexError:
    print("Error")
    a = int(input("Input the first number: "))
    b = int(input("Input the second number: "))
    add(a,b)
    raise(SystemExit)

add(a,b)