for x in range(9,0,-1):
    print("#", x,"단", "#", end="\t")
print()

for i in range(9,0,-1):
    for j in range(9,0,-1):
        print(j, "x", i, "=", j*i, end="\t")
    print()
## 왜 마지막에 print() 를 쓰지 않으면 여백이 안맞는걸까