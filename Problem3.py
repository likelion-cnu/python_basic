for i in range(9, 0, -1):
    print(f"#  {i}단  #", end = " ")
print()

for j in range(9, 0, -1):
    for i in range(9, 0,-1):
        print("{} * {} = {: >2}".format(i, j, i * j), end = "  ")
    print()