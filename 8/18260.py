from itertools import product
a = product("0123456789ab", repeat=6)
c=0
for i in a:
    num = "".join(i)
    if num[0]!= "0":
        if num.count("b") == 1:
            ch = 0
            nech =0
            for i in num:
                if int(i, 36) % 2 == 0:
                    ch+=1
            if ch == 3:
                c+= 1
print(c)

