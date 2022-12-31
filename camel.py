word = input('camelCase:')
for each in word:
    if each.isupper():
       word = word.replace(each,'_'+each.lower())
print(f'snake_case:{word}')
