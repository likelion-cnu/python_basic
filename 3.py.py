
for i in reversed(range(1, 10)):

    print ("#  %d 단  #" %(i) , end="\t") 

 

for b in reversed(range(1, 10)):

    print(" ")

    for a in reversed(range(1, 10)):

        print ("%2d * %2d = %2d" %(a, b, a*b), end="\t")

        

print(" ")