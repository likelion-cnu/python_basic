for i in range(9, 0, -1):
    print("#  %d단  #" %i, end="\t")
print()

for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        print("%d * %d = %d" %(j, i, i*j), end="\t")
    print()