# 문제2
order={"Num": "101", "Buger":"치즈버거","Beverage":"콜라"}

# 주문 내역 조회
for key, value in order.items():
    print(key, value)

# 주문 수정 사항
order["Buger"] = "더블치즈버거"
order["Side"] = "치킨너겟"

# 주문 내역 삭제
order.clear()

# 주문 추가
order = [{"Num":"102", "Buger":"불고기버거세트", "Beverage":"바닐라쉐이크"},
         {"Num":"103", "Buger":"치킨버거", "Beverage":"딸기칠러", "Side":"치즈스틱"}]