def extgcd1(a, b):
    # Recursive version
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extgcd1(b, a % b)
        return gcd, y, x - (a // b) * y
def extgcd2(a, b):
    # Iterative version
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0
