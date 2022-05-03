a = 0
b = 0
for a in range(9,0,-1):
    print("# %d단 #" %a, end="")
for b in range(9,0,-1):
    for a in range(9,0,-1):
        print("%d X %d = %d" %(a,b,a*b), end="\t")
   