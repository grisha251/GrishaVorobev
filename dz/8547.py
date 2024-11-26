print("a b c t")
for a in range(2):
        for b in range(2):
            for c in range(2):
                for t in range(2):
                    f =((not(a))or(not(b)))and(c<= (not(a))) and(t and(not(a))or c and (not(b)))
                    if f == True or f == False:
                        print(a, b, c, t, f)