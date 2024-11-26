k = 0
for n in range(1, 1000):
    b = hex(n)[2:]
    if b.count("b") %2 ==0:
        b ="1" + b
    else:
        b= b + "1"
    r = int(b, 16)
    if r // 100 == 0 and r // 10 != 0:
        k+=1

print(k)