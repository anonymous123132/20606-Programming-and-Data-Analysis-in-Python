def gcd(p,q):
    n= min(q,p)
    for i in reversed(range(1,n)):
        if n% i== 0:
            return i
        else:
            return n

def gcd1(p, q):
    n = min(p, q);
    found = False
    while not found:
        if p % n == 0 and q % n == 0:
            found = True
        else:
            n -= 1
    return n

