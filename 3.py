for n in range(9,0,-1):
    print("#  %d단  #"%(n),end="\t")
print("")

for i in range(9,0,-1):
    for j in range(9,0,-1):
        print(j,"*",i,"=",j*i,end="\t")
    print("")