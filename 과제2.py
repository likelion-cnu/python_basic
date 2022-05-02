
order = {"Num": "101", "Buger":"치즈버거","Beverage":"콜라"} 

for key, val in order.items():
        print("{} : {}".format(key,val)) 

order["Buger"]= "더블치즈버거"
order["Side"] = "치킨너겟"

order.clear()

order =[{"주문번호":102, "버거":"불고기버거세트", "음료":"바닐라쉐이크"},
{"주문번호":103, "버거":"치킨버거", "음료":"딸기칠러", "사이드":"치즈스틱"}]
print(order)
