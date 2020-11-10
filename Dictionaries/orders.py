from collections import defaultdict

products = input().split()

price_products = defaultdict(float)
product_quantity = defaultdict(int)

while True:
    command = products
    if command[0] == 'buy':
        break

    type_product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    price_products[type_product] = price
    product_quantity[type_product] += quantity

    products = input().split()

for k, n in price_products.items():
    total = n * product_quantity[k]
    print(f'{k} -> {total:.2f}')
