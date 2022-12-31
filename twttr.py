word = input('Input:')
for each in word:
    if each.lower() not in 'aeiou':
        print(each,end='')