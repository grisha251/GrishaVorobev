from itertools import product
a = product("01234567", repeat=5)
c=0
for i in a:
    num = "".join(i)
    if num[0] !="0":
        if int(num[0]) % 2 == 0:
            if num[4] != "2" and num[4] != "6":
                if num.count("7") <= 2:
                    c+=1
print(c)