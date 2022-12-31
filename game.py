import random
while True:
 try:
    level = int(input("Level: "))
    if level > 0:
      break
    else:
      continue
 except ValueError:
        pass
ran = random.randint(1,level)
while True:
    while True:
      try:
       guess = int(input("Guess: "))
       if guess > 0:
         break
       else:
        continue

      except ValueError:
         pass
    if guess > ran:
      print('Too large!')
    elif guess < ran:
      print("Too small!")
    else:
      print('Just right!')
      break

