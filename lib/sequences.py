#!/usr/bin/env python3

def print_fibonacci(length):
    if (length<=0):
        print([])
    elif(length==1):
        print([0])
    elif(length==2):
        print([0,1])
    else:
        fibonacci=[0,1]
        for i in range(2,length):
           fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
        print(fibonacci)

print_fibonacci(9)