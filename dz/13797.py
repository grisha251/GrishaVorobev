print("w x y z")
for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = ((not(x)) and(z<= y) and(not(w)))or ((z==w)and(x or y <= w))
                    if f == True:
                        print(w, x, y, z, f)