def t(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s

for n in range(1, 100):
    s = t(n)
    if n % 2 == 0:
        s = '2' + s + t(2*(n % 3))
    else:
        s = t(2*int(s[0])) + s + '2'
        r = int(s, 3)
        if r > 100:
            print(r)