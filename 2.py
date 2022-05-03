## 1. 현재 주문내역을 for문을 이용해 키와 값으로 분리해서 조회해 주세요!
order={"Num":"101", "Buger":"치즈버거", "Beverage":"콜라"}
for x,y in order.items():
    print(x + ":", y)

## 2. 주문 수정사항이 있어요. 요청사항대로 변경해 주세요!    
order["Buger"]="더블치즈버거"
order["사이드메뉴"]="치킨너겟"
print(order)

## 3. 음식이 완성되었습니다. 주문서에 내역을 삭제해 주세요
order.clear()
print(order)

## 4. 새로운 주문들이 들어왔어요. order=[] 리스트주문서에 추가해주세요!
order=[]
order.append("주문번호:102")
order.append("버거:불고기버거세트")
order.append("음료:바닐라쉐이크")
print(order)

del order[0:2]
order.append("주문번호:103")
order.append("버거:치킨버거")
order.append("음료:딸기칠러")
order.append("사이드:치즈스틱")
print(order)





