# 1. 첫 주문 출력
order = {"Num": "101", "Buger":"치즈버거","Beverage":"콜라"}
for x, y in order.items():
    print(x + " : " + y)

# 2. 주문 수정
order["Buger"] = "더블치즈버거"
order["Side menu"] = "치킨너겟"
print(order)

# 3. order 내역 삭제
del order

# 4. 새로운 주문을 리스트에 담기
order = []
order.append({"Num" : "102", "Burger" : "불고기버거세트", "Beverage" : "바닐라쉐이크"})
order.append({"Num" : "103", "Burger" : "치킨버거", "Beverage" : "딸기칠러", "Side menu" : "치즈스틱"})
print(order)