#문제2
order={"Num":"101", "Burger":"치즈버거", "Beverage":"콜라"}

#문제2-1
for x,y in order.items():
    print(x + " : " + y)
print() #줄바꿈 구분용

#문제2-2
order.update(Burger="더블치즈버거")
order["Sidemenu"]="치킨너겟"
print(order)
print() #줄바꿈 구분용

#문제2-3
#주문서 항목 모두 삭제!
order.clear()
print(order)
print() #줄바꿈 구분용

#문제2-4, order=[] 리스트주문서에 추가(리스트안에 딕셔너리 사용하였음)
order=[]
order.append({"Num":"102", "Burger":"불고기버거세트", "Beverage":"바닐라쉐이크"})
order.append({"Num":"103", "Burger":"치킨버거", "Beverage":"딸기칠러", "사이드":"치즈스틱"})
print(order)