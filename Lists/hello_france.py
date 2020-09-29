items_with_their_prices = input().split('|')
budget = int(input())

total_spend = 0
total_spend_with_percentage = 0

for items in items_with_their_prices:
    item = items.split('->')

    product_name = item[0]
    price = float(item[1])

    if budget < price:
        continue

    if product_name == 'Clothes':
        if price <= 50:
            budget -= price
            total_spend += price
            price_clothes = price * 1.40
            total_spend_with_percentage += price_clothes
            print(f'{price_clothes:.2f}', end=' ')

    elif product_name == 'Shoes':
        if price <= 35:
            total_spend += price
            budget -= price
            price_shoes = price * 1.40
            total_spend_with_percentage += price_shoes
            print(f'{price_shoes:.2f}', end=' ')

    elif product_name == 'Accessories':
        if price <= 20.50:
            total_spend += price
            budget -= price
            price_accessories = price * 1.40
            total_spend_with_percentage += price_accessories
            print(f'{price_accessories:.2f}', end=' ')

    else:
        continue


profit = abs(total_spend - total_spend_with_percentage)

print()
print(f'Profit: {profit:.2f}')

if total_spend_with_percentage + budget >= 150:
    print(f'Hello, France!')
else:
    print(f'Time to go.')