order = {"Num":"101", "Burger":"치즈버거", "Beverage":"콜라"}
for k in order:
    val=order[k]
    print("%s : %s" %(k,val))

order["Burger"] = "더블치즈버거"
order["Side"] = "치킨너겟"
print(order)

order.clear()
print(order)

order = []
order.append({"Num":"102", "Burger":"불고기버거세트", "Beverage":"바닐라쉐이크"})
order.append({"Num":"103", "Burger":"치킨버거", "Beverage":"딸기칠러", "side":"치즈스틱"})
print(order)