from itertools import product
a = product("01234567", repeat=7)
c=0
for i in a:
    num = "".join(i)
    if num[0]  != "0":
        f = 0
        for i in num:
            if int(i)% 2 == 0:
                f +=1
        if f == 2:
            num = num.replace("1","*")
            num = num.replace("3","*")
            num = num.replace("5","*")
            if "*7" not in num and "77" not in num and "7*" not in num:
                c+=1


print(c)