print("w x y z")
for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = ((x<=y)or (z==x))and(w<=z)
                    if f == True or f == False:
                        print(w, x, y, z, f)