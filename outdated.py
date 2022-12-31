def date():
 months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
 while True:
  try:
   date_inp = input('Date:')
   word_format = []
   for each in date_inp.split(" "):
     if each in months:
      if date_inp.replace(',','') == date_inp:
        date_inp = int(date_inp)
      for each in date_inp.replace(',','').split(' '):
       if each in months:
        word_format.append(months.index(each)+1)
        continue
       word_format.append(int(each))
      return final_format(word_format)
   num_format = [int(each) for each in date_inp.split("/")]
   return final_format(num_format)
  except ValueError:
    pass

def final_format(lst):
  if lst[0] <= 12:
     if lst[1] <= 31:
         if lst[0] < 10 and lst[1] < 10:
             return f'{lst[2]}-0{lst[0]}-0{lst[1]}'
         elif lst[0] < 10:
             return f'{lst[2]}-0{lst[0]}-{lst[1]}'
         elif lst[1] < 10:
             return f'{lst[2]}-{lst[0]}-0{lst[1]}'
         else:
             return f'{lst[2]}-{lst[0]}-{lst[1]}'
     else:
       return date()
  else:
    return date()

print(date())