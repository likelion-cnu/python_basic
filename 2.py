order={"Num": "101", "Buger":"치즈버거","Beverage":"콜라"}

print("\n--------------\n")
print("현재 주문내역")    
print("\n--------------\n")
for key, value in order.items():
    print(key,":",value)   

print("\n--------------\n")
print("주문 수정사항")
print("\n--------------\n")
order["Buger"]="더블치즈버거"
order["사이드메뉴"]="치킨너겟"

for key, value in order.items():
    print(key,":",value) 

print("\n--------------\n")
print("주문서에 내역 삭제")
print("\n--------------\n")
order.clear()

print("\n--------------\n")
print("새로운 주문")
print("\n--------------\n")
order1={"주문번호":"102", "버거":"불고기버거세트", "음료":"바닐라쉐이크"}
order2={"주문번호":"103", "버거":"치킨버거", "음료":"딸기칠러", "사이드":"치즈스틱"}

for key, value in order1.items():
    print(key,":",value) 
print("\n")

for key, value in order2.items():
    print(key,":",value) 
print("\n")

