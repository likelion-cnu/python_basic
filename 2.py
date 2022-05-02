order={"Num": "101", "Buger":"치즈버거","Beverage":"콜라"}

for key, value in order.items():
    print(key, value, sep=' : ')

order["Burger"]="더블치즈버거"
order["Extra"]="치킨너겟"
print(order)

order.clear()
print(order)

order = [{"Num":"102", "Burger":"불고기버거세트", "Beverage" : "바닐라쉐이크"},
         {"Num":"103", "Burger":"치킨버거", "Beverage":"딸기칠러", "Extra":"치즈스틱"}]
print(order)