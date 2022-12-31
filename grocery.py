grocery_list = []
while True:
    try:
        items = input().upper()
        grocery_list.append(items)
    except EOFError:
        grocery_list.sort()
        dct = {each:grocery_list.count(each) for each in grocery_list}
        for keys,values in dct.items():
            print(f'{values} {keys}')
        break