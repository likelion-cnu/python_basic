#문제3

for a in range(9, 0, -1):
    print("#  ",a,"단  #", end="\t")
print()

for a in range(9, 0, -1):
    for b in range(9, 0, -1):
        print(a,"*",a,"=",a*b,end="\t")
print()