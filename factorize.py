#!/usr/bin/python3

import time
import math
import sys

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    
    x = 2
    y = 2
    d = 1 
    f = lambda x: (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)

    return d

def main():
    if len(sys.argv) != 2:
        print("Usage: python factorize.py <number>")
        return

    num = int(sys.argv[1])

    if num <= 1:
        print(f"{num} is not factorizable.")
        return

    factor = pollard_rho(num)

    if factor == num:
        print(f"{num} is prime.")
    else:
        print(f"{num}={factor}*{num // factor}")

if __name__ == '__main__':
    main()
