def t(x):
    b = ''
    while x:
        b = str(x % 6) + b
        x //= 6
    return b
s = []
for n in range(1,1000):
    b = t(n)
    if int(n) % 3 ==0:
        b = b +b[2:]
    else:
        g = (int(n)%3) * 10
        b = b + t(g)
    r = int(b, 6)
    if r >680:
        s += [r]
        print(min(s))
