order={"Num": "101", "Burger":"치즈버거", "Beverage":"콜라"}
order_list=[]
Num=int(101)


#1.현재주문내역
def orderlist():
    print("주문을 알려드립니다")
    for keys, values in order.items():
       print(keys, ":", values)

orderlist()
        
#2.주문수정
print("2. 주문수정")
order['Burger'] = "더블치즈버거" 
order['Sidemenu'] = "치킨너겟"
orderlist()


# 3. 주문내역삭제
order.clear()


# 4. 추가주문, 리스트에 추가
while True:
    new=input("주문하시겠습니까? (y/n) ")
    if new=="n":
        break
    elif new=="y":
        Num=int(Num+1)
        Burger=input("버거이름을 입력해주세요: ")
        Beverage=input("음료이름을 입력해주세요: ")
        Sidemenu=input("추가하실 사이드메뉴를 입력해주세요: ")
        order_list.append([{"Num" : Num, "Burger" : Burger, "Beverage" : Beverage, "Side Menu" : Sidemenu}])
        print(order_list)
    else:
        "다시 입력해주세요"