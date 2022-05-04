order = {"Num": "101", "Burger": "치즈버거", "Beverage":"콜라"}

#1조회
for key, value in order.items():
    print (key, value)

#2수정
order["Burger"] = "더블치즈버거"
order["Side"]= "치킨너겟"

#3삭제
order.clear()

#4추가
order = []
order.append ({"Num": "102", "Burger": "불고기버거세트", "Beverage":"바닐라쉐이크"})
order.append ({"Num": "103", "Burger": "치킨버거", "Beverage":"딸기칠러", "Side":"치즈스틱"})