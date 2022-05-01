for i in range(9, 0, -1):
    print("# {0}단 # ".format(i), end="")
    
print("\n")

for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        if j == 1:
            print("{0} * {1}={2} ".format(j, i, j*i), end="")
            print("\n")
        else:
            print("{0} * {1}={2} ".format(j, i, j*i), end="")

            
