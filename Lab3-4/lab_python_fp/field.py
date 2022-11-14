def field(items, *args):

    assert len(args) > 0
    if len(args) == 1:
        for dict in items:
            curr = dict.get(args[0])
            if curr is not None:
                yield curr
    else:
        for elem in items:
            dict = dict()
            for arg in args:
                curr = elem.get(arg)
                if curr is not None:
                    dict[arg] = curr
            if len(dict) != 0:
                yield dict

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 3000, 'color': 'black'},
        {'title': 'Диван для отдыха', 'price': 10000, 'color': 'grey'},
        {'title': 'Стул', 'price': 1000, 'color': 'white'},
        {'title': None, 'price': None, 'color': 'red'}
    ]
    lst1 = []
    lst2 = []

    for elem in field(goods, 'title'):
        lst1.append(elem)

    for elem in field(goods, 'title', 'price','color'):
        lst2.append(elem)

    print(lst1)
    print(lst2)
