print("1. 현재 주문내역 조회")
order={"Num": "101", "Buger":"치즈버거","Beverage":"콜라"}
for key, value in order.items():
    print("%s: %s"%(key,value))
print("\n")

print("2. 주문 변경")
order["Buger"] = "더블치즈버거"
order["Side"] = "치킨너겟"
for key, value in order.items():
    print("%s: %s"%(key,value))
print("\n")

print("3. 주문 삭제")
order.clear()
print(order)
print("\n")

print("4. 새로운 주문 추가")
order=[]
while True:
    ans = input("새로운 주문 입력(y/n) : ")
    if ans == "n":
        break
    elif ans == "y":
        num = input("주문번호 : ")
        burger = input("버거 : ")
        beverage = input("음료 : ")
        side = input("사이드 : ")
        order.append({"Num" : num, "Burger" : burger, "Beverage" : beverage, "Side" : side})
    else:
        print("다시 입력해주세요.")
print(order)