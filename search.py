def searching(name):
    counter = 0
    with open('results.csv', 'w',  encoding='UTF-8') as res:
        res.close()
    with open('book.csv', 'r',  encoding='UTF-8') as f:
        line_count = sum(1 for line in open('book.csv'))
        for i in range(line_count):
            a = f.readline()
            if a.count(name) == 1:
                counter += 1
                with open('results.csv', 'a',  encoding='UTF-8') as r:
                    r.write(a)
        if counter > 0:
            print(f'По Вашему запросу найдено записей : {counter}')
        else:
            print('По Вашему запросу ничего не найдено')
