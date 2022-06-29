import math
import random

def ES_COMPUESTO(a, n, t, u):
    x = POW_MOD(a, u, n)

    if (x == 1 or x == n - 1):
        return False

    for i in range(1,t,1):
        x = POW_MOD(x, 2, n)
        if (x == n - 1):
            return False

    return True


def EUCLIDES(a, b):
    if b == 0:
        return a
    else:
        return EUCLIDES(b, a % b)
    
def EUCLIDES_EXTEND(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, dx, dy) = EUCLIDES_EXTEND(b, a % b)
        (x, y) = (dy, dx - a // b * dy)
        return (d, x, y)

def EXP_MOD(a, x, n):
    c = a % n
    r = 1
    while x > 0:
        if x % 2 == 1:
            r = (r * c) % n
        c = (c * c) % n
        x = x // 2
    return r

def INVERSO(a, n):
    (mcd, x, y) = EUCLIDES_EXTEND(a, n)
    if mcd == 1:
        return x % n
    else:
        return None

def MILLER_RABIN(n, s):
    t = 0
    u = n - 1
    while (u % 2 == 0):
        u = u / 2
        t = t + 1

    j = 1
    while (j < s):
        a = RANDOMINTEGER(2, n - 1)
        if (ES_COMPUESTO(a, n, t, u)):
            return False
            
        j += 1

    return True

def POW_MOD(a, x, n):
    c = a % n
    r = 1
    
    while(x > 0):
        if((x % 2) != 0):
            r = (r * c) % n
        
        c = (c * c) % n
        x = int(x / 2)
    
    return r

def RANDOMBITS(b):
    max = pow(2, b) - 1
    n = RANDOMINTEGER(0, max)
    m = pow(2, b - 1) + 1
    n = n | m
    return n

configure_s = 40

def RANDOMGEN_PRIMOS(b):
    s = configure_s
    n = RANDOMBITS(b)
    while (not MILLER_RABIN(n, s)):
        n += 2
  
    return n

def RANDOMINTEGER(min, max):
    return random.randint(min, max)

def RSA_KEY_GENERATOR(bits):
    arg = bits // 2
    p = RANDOMGEN_PRIMOS(arg)
    q = RANDOMGEN_PRIMOS(arg)
    while p == q:
        q = RANDOMGEN_PRIMOS(arg)

    n = p * q
    phiN = (p - 1) * (q - 1)
    
    e = RANDOMBITS(bits)
    while EUCLIDES(e, phiN) != 1:
        e = RANDOMBITS(bits)
    
    d = INVERSO(e, phiN)
    return (e, n), (d, n)

def CIPHER(m, k: tuple):
    arg1, arg2 = k
    return EXP_MOD(m, arg1, arg2)

def main():
    k = 64
    P, S = RSA_KEY_GENERATOR(k)
    e, n = P
    d, _ = S

    tab = 62
    print('e = {:}\nd = {:}\nn = {:}\n'.format(e, d, n))
    print('-' * tab)
    print('{:^20}{:^20}{:^20}'.format('m', 'c = P(m)', 'm\' = S(c)'))
    print('-' * tab)

    stack = []
    for i in range(10):
        m = RANDOMBITS(32)
        while m in stack:
            m = RANDOMBITS(32)
        stack.append(m)
        c = CIPHER(m, P)
        print('{:^20}{:^20}{:^20}'.format(m, c, CIPHER(c, S)))

main()
