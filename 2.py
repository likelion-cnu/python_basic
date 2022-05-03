## 문제 2

order={"Num": "101", "Buger":"치즈버거","Beverage":"콜라"}

for i in order:
    print(i, ':', order[i])

print()

order["Buger"] = "더블치즈버거"
order['Side'] = '치킨너겟'

print(f'주문 수정 사항: {order}')

print()

order.clear()

print('주문 내역 삭제: ', order)

print()

order = []
a = {"Num":102, "Buger":"불고기버거세트","Beverage":"바닐라쉐이크"}
b = {"Num":103, "Buger":"치킨버거","Beverage":"딸기칠러", 'Side':'치즈스틱'}
                
order.append(a)
order.append(b)

print(order)
