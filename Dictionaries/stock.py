def get_stock(raw_data):
    data = raw_data.split(' ')
    return {data[i]: (int(data[i + 1])) for i in range(0, len(data), 2)}


def check_availability(stock: dict, search_products: list):
    for product in search_products:
        if not stock.get(product):
            print(f'Sorry, we don\'t have {product}')
        else:
            print(f'We have {stock[product]} of {product} left')


stock = get_stock(input())
check_availability(stock, input().split(' '))