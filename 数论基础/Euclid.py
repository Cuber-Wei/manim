def gcd1(a, b):
    # Recursive version
    if b == 0:
        return a
    else:
        r = gcd1(b, a % b)
        return r
def gcd2(a, b):
    # Iterative version
    while b != 0:
        a, b = b, a % b
    return a
