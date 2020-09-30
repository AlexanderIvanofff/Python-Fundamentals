def solve(product, count):
    price = None
    if product == 'coffee':
        price = 1.50
    elif product == 'water':
        price = 1.00
    elif product == 'coke':
        price = 1.40
    elif product == 'snacks':
        price = 2.00

    if price is not None:
        return price * count


current_product = input()
count_product = int(input())
print(f'{solve(current_product, count_product):.2f}')