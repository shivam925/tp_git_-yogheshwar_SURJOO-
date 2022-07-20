#!/usr/bin/python3

import sys

def add(a, b):
    x = a + b
    return x

try: 
    a = int( sys.argv[1] )
    b = int( sys.argv[2] )
except IndexError:
    print("Error")
    raise(SystemExit)

print(add(a,b))