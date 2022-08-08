products_dict = {
    "product0": {'id': 'product0', 'name': 'Mine', 'price': 48547, 'owned': 10},
    "product1": {'id': 'product1', 'name': 'Factory', 'price': 261477, 'owned': 5},
    "product2": {'id': 'product2', 'name': 'Bank', 'price': 1400000, 'owned': 1},
    "product3": {'id': 'product3', 'name': 'Temple', 'price': 20000000, 'owned': 0},
}

products_list = list(products_dict.values())[::-1]
for row in products_list:
    print(row)


for i, product in enumerate(products_list):
    if i == 0:
        pass

    elif products_list[i]["owned"] - products_list[i-1]["owned"]:
        row["id"].click()
        print(f"Bought product {row['name']}")
        break