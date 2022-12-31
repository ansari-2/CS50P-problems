import inflect
sequence = inflect.engine()
lst = []
greet = 'Adieu, adieu, to'
while True:
    try:
        inp = input('Name: ')
        lst.append(inp)
    except EOFError:
        break
names = sequence.join(lst)
print(greet,names)



