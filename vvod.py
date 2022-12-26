def writing_phone_book(data):
    with open('book.csv', 'a', encoding='UTF-8') as f:
        f.write(data)
        f.write('\n')