import random


def main():
    n = 0
    count = 0
    score = 10
    lvl = get_level()
    while n < 10:
       X = generate_integer(lvl)
       Y = generate_integer(lvl)
       Z = X + Y
       while True:
        try:
          ans = int(input(f'{X} + {Y} = '))
          if ans != Z:
             count += 1
             if count % 3 != 0:
               print('EEE')
               continue
             else:
                score -= 1
                print('EEE')
                print(f'{X} + {Y} = {Z}')
                break
          else:
             break
        except ValueError:
            count += 1
            print('EEE')
        else:
            break
       n += 1
    print('Score:',score)

def get_level():
  while True:
   try:
    level = int(input('Level: '))
    if level < 1 or level > 3:
        continue
    else:
        return level
   except ValueError:
        pass


def generate_integer(level):
   if level == 1:
    integer = random.randint(0,9)
    return integer
   elif level == 2:
    integer = random.randint(10,99)
    return integer
   else:
    integer = random.randint(100,999)
    return integer



if __name__ == "__main__":
    main()