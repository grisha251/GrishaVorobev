def t(x):
    b = ''
    while x:
        b = str(x % 7) + b
        x //= 7
    return b
k = 0
for i in range(343,2401):
    b = t(i)
    if int(b[-1])%2 ==0:
        b = "6" + b
    else:
        b = b + "5"
    r = int(b, 7)
    if r > 14500:
        k+=1
print(k)
