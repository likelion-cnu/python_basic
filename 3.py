for l in range(1,10):
    print("*****", end="\t")
print(" ")

for m in range(1,10):
    print(" %d단 "%(10-m),end="\t")
print(" ")

for n in range(1,10):
    print("*****",end="\t")
print(" ")

for b in range(1,10):
    for a in range(2,11):
        c=11-a
        d=10-b
        print("%d*%d=%d" %(c,d,c*d), end="\t")
    print(" ")    

