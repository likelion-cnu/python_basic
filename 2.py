order={"Num": "101", "Buger":"치즈버거", "Beverage":"콜라"}


oreder_values = []

# 1. 현재 주문내역을 for문을 이용해 키와 값으로 분리해서 조회해 주세요!
for keys, values in order.items():
    print("{0} : {1}".format(keys, values))
    
    
# 2. 주문 수정사항이 있어요. 요청사항대로 변경해 주세요!
order['Burger'] = "더블치즈버거" 
order['SideMenu'] = "치킨너겟"


# 3. 음식이 완성되었습니다. 주문서에 내역을 삭제해 주세요!
order.clear()


# 4. 새로운 주문들이 들어왔어요. order=[] 리스트주문서에 추가해주세요!
for i in range(2):    
    if i == 0:
        order["Num"] = 102
        oreder_values.append(102)
        
        order["Buger"] = "불고기버거세트"
        oreder_values.append("불고기버거세트")
        
        order["Beverage"] = "바닐라쉐이크"
        oreder_values.append("바닐라쉐이크")
    
    if i == 1:
        order["Num"] = 103
        oreder_values.append(103)
        
        order["Buger"] = "치킨버거"
        oreder_values.append("치킨버거")
        
        order["Beverage"] = "딸기칠러"
        oreder_values.append("딸기칠러")
        
        order["SideMenu"] = "치즈스틱"
        oreder_values.append("치즈스틱")
