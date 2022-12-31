def num():
  while True:
   try:
     inp = input("Fraction:")
     x,y = int(inp[:inp.index('/')]),int(inp[(inp.index('/') + 1):])
     if x <= y:
      z = x/y
      return z
   except ValueError:
      pass
   except ZeroDivisionError:
      pass

fract = num() * 100
if fract >= 99:
  print('F')
elif fract <= 1:
  print('E')
else:
  fract = '{0:.0f}'.format(fract)
  print(f'{fract}%')


