from itertools import product
a = product("0123456789abcdef", repeat=5)
c=0
for i in a:
    num = "".join(i)
    if num[0] != "0":
        if num.count("6") == 2:
            for i in "0248ace":
                num = num.replace(i, "*")
            if "6*" not in num and "*6" not in num and "66" not in num:
                c+= 1
print(c)