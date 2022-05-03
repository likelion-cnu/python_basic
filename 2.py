#문제2

order={"Num": "101", "Buger":"치즈버거","Beverage":"콜라"}
 
for key, value in order.items():
    print(key, value)

order["Buger"] = "더블치즈버거"
order["Sidemenu"] = "치킨너겟"

order.clear()

order = [{"Num":"102", "Buger":"불고기버거세트", "Beverage":"바닐라쉐이크"},
         {"Num":"103", "Buger":"치킨버거", "Beverage":"딸기칠러", "Sidemenu":"치즈스틱"}]

print(order)