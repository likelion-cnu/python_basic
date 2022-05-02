order = {"Num": "101", "Buger": "치즈버거", "Beverage": "콜라"}

for key, value in order.items():
    print(f"{key} : {value}")

order["Buger"] = "더블치즈버거"
order["Side Menu"] = "치킨너겟" 

order.clear()

order = []
order.append({"Num": "102", "Buger": "불고기버거세트", "Beverage": "바닐라쉐이크"})
order.append({"Num": "103", "Buger": "치킨버거", "Beverage": "딸기칠러", "Side Menu": "치즈스틱"})