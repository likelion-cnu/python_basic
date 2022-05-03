order={"Num": "101", "Buger":"치즈버거","Beverage":"콜라"}

for x,y in order.items():
    print(x)
    print(y)

order["Burger"] = "더블치즈버거"
order["Side-menu"] = "치킨너겟"

order.clear()

order = []
order.append("Num": "102", "Buger": "불고기버거세트", "Beverage":"바닐라쉐이크")
order.append("Num": "103", "Buger": "치킨버거", "Beverage": "딸기칠러", "Side-meun": "치즈스틱")
