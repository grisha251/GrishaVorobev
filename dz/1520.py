print("a b c t")
for a in range(2):
        for b in range(2):
            for c in range(2):
                f = (a<=b)and(a and b <= (not(c)))
                if f == True or f == False:
                    print(a, b, c, f)