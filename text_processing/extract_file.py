def result(data):
    current_data = data.split('\\')
    last_items = current_data[-1]
    split_item = last_items.split('.')
    name = split_item[0]
    extension = split_item[1]
    return f'File name: {name}\nFile extension: {extension}'


print(result(input()))