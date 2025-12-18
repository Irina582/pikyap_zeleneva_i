def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        # Если один аргумент - возвращаем только значения
        key = args[0]
        for item in items:
            if key in item and item[key] is not None:
                yield item[key]
    else:
        # Если несколько аргументов - возвращаем словари
        for item in items:
            result = {}
            has_valid_fields = False
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
                    has_valid_fields = True
            if has_valid_fields:
                yield result


if __name__ == '__main__':
    # Тестирование
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': 'Стол', 'price': None, 'color': 'white'},
        {'price': 5000}
    ]

    print("Test 1 - один аргумент:")
    for item in field(goods, 'title'):
        print(item)

    print("\nTest 2 - несколько аргументов:")
    for item in field(goods, 'title', 'price'):
        print(item)