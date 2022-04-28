order = {"Num": "101", "Burger":"치즈버거","Beverage":"콜라"}

for i in order:
    print(i,":",order[i]) 
print("================================")

order["Burger"] = "더블치즈버거"
order["Sidemenu"] = "치킨너겟"

for i in order:
    print(i,":",order[i]) 
print("================================")

order.clear

order = []

order.append({"Num":"102", "Burger":"불고기버거세트", "Beverage":"바닐라쉐이크"})
order.append({"Num":"103", "Burger":"치킨버거", "Beverage":"딸기칠러", "SideMenu":"치즈스틱"})

for i in order:
    print(i)