print("#   9단   #\t#   8단   #\t#   7단   #\t#   6단   #\t#   5단  #\t#   4단   #\t#   3단   #\t#   2단   #\t#   1단  #")
for i in range(1, 10):
    for j in range(1, 10):
        print(str(10 - i) + " * " + str(10 - j) + " = " + str((10 - i) * (10 - j)) + "\t", end='')
    print()