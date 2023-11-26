#!/usr/bin/python3

from functools import reduce
from math import sqrt

def factors_1(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))

import itertools

def isprime(n, lp):
    for i in lp:
        j = int(i)
        if n % j == 0:
            if j == n:
                return 1
            return j
    divs = range(1000001, int(n ** 0.5) + 1, 2)
    return [d for d in itertools.chain(divs[::3], divs[1::3]) if n % d == 0][0]

def gen_primes(n):
    D = {}
    q = 2

    while q <= n:
        if q not in D:
            D[q * q] = [q]
            yield q
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def factor(n, lp):
    if n in lp:
        return 1

    for j in lp:
        if n % j == 0:
            return j

    # Trial division with primes up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i

    def rho_factorization(n):
        if n % 2 == 0:
            return 2

        x, y, d = 2, 2, 1
        f = lambda x: (x ** 2 + 1) % n

        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)

        return d

    # Try Pollard's rho factorization followed by trial division
    result = rho_factorization(n)
    if result == 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return i

    return result
