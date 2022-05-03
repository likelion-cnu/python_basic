for i in range(9, 0, -1):
    print("#  ",i,"단  #", end="\t")
print()

for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        print(j,"*",i,"=",i*j,end="\t")
    print()