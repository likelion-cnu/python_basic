#문제3
#range([start], stop, [step]) : start와 step은 생략가능, 이때 start와 step은 생략시 0,1로
#step은 숫자 사이의 거리를 의미한다.
#아래와 같은 경우 시작이 9 끝이 0으로 step이 -1씩 차감되는 for문이다.
#Exception has occured : TypeError, can only concatenate str to str -> 숫자를 문자로 변환해주어야 함
for i in range(9,0,-1):
    print("#  " + str(i) + "단"  + "  #", end = '\t')
print()

for y in range(9,0,-1): 
    for x in range(9,0,-1):
        print(x, "*", y, '=',  x* y, end = '\t')  
        if(x == 1):
            print()
