def morloc_and(x, y):
    return x & y

def morloc_or(x, y):
    return x | y

def morloc_xor(x, y):
    return x ^ y

def morloc_shiftl(x, n):
    return x << n

def morloc_shiftr(x, n):
    return x >> n

def morloc_bnot(x):
    return ~x

def morloc_testBit(x, n):
    return (x >> n) & 1 == 1

def morloc_setBit(x, n):
    return x | (1 << n)

def morloc_clearBit(x, n):
    return x & ~(1 << n)

def morloc_flipBit(x, n):
    return x ^ (1 << n)

def morloc_popcount(x):
    return bin(x & 0xFFFFFFFFFFFFFFFF).count('1')
