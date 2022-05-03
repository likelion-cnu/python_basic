# 첫 줄 출력
for i in range(9, 0, -1):
    num = str(i)
    print("#  " + num + "단" + "  #  ", end="")
    print("\n")

# 구구단 출력
for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        first = str(i)
        second = str(j)
        print(second + " * " + first + "=" + str(i*j), end="  ")
    print("\n")