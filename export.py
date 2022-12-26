def export_contacts(data, separator):
    with open(f'{data}', 'r', encoding='UTF-8') as file:
        line_count = sum(1 for line in open(f'{data}'))
        for i in range(line_count):
            a = file.readline().split('; ')
            print(f'{separator}'.join(a))
