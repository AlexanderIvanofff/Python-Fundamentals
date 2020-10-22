books_in_library = input().split('&')


while True:
    command = input()
    if command == 'Done':
        break

    tokens = command.split('|')
    instructions = tokens[0].strip()
    book = tokens[1].strip()

    if instructions == 'Add Book':
        if book not in books_in_library:
            books_in_library.insert(0, book)
        else:
            continue

    elif instructions == 'Take Book':
        if book in books_in_library:
            books_in_library.remove(book)
        else:
            continue

    elif instructions == 'Swap Books':
        second_book = tokens[2].strip()

        if book in books_in_library and second_book in books_in_library:
            first_book_index = books_in_library.index(book)
            second_book_index = books_in_library.index(second_book)
            books_in_library[first_book_index], books_in_library[second_book_index] \
                = books_in_library[second_book_index], books_in_library[first_book_index]

    elif instructions == 'Insert Book':
        books_in_library.append(book)

    elif instructions == 'Check Book':
        index = int(book)
        if index in range(len(books_in_library)):
            print(books_in_library[index])
        else:
            continue

print(f'{", ".join(books_in_library)}')