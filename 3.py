# 문제3

# 단 출력
for n in range(9, 0, -1):
    print("#  ", n, "단", "  #", end = "\t")
print("\n")

# 구구단 출력
for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        print(j, " * ", i, "=", i * j, end = "\t")
    print("\n")