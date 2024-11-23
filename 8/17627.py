from itertools import product
a = product("0123456789abcde", repeat=5)
c=0
for i in a:
    num = "".join(i)
    if num[0] != "0":
        if num.count("8") == 1:
            f = 0
            for i in num:
                if int(i, 36) > 9:
                    f += 1
            if f >=2:
                c+=1
print(c)