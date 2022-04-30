for i in range(9,0,-1):
    print("#%3d단  #" %i, end=" ")
print()
for i in range(9,0,-1):
    for j in range(9,0,-1):
        print("%2d * %d=%2d" %(j,i,j*i), end=" ")
    print()