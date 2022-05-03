def print_orders(orders):
    for order in orders:
        for key, value in order.items():
            print(key + " : " + value)
    print()


order = {"Num": "101", "Burger": "치즈버거", "Beverage": "콜라"}
orders = [order]


# 1
print_orders(orders)

# 2
order["Burger"] = "더블치즈버거"
order["SideMenu"] = "치킨너겟"

print_orders(orders)

# 3
orders.remove(order)

print_orders(orders)

# 4
orders.append({"Num": "102", "Burger": "불고기버거세트", "Beverage": "바닐라쉐이크"})
orders.append({"Num": "103", "Burger": "치킨버거", "Beverage": "딸기칠러", "SideMenu": "치즈스틱"})

print_orders(orders)

input()