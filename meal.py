def main():
     time=input('What time is it? ')
     time=convert(time)
     if time>=7 and time<=8:
          return 'breakfast time'
     elif time>=12 and time<=13:
          return 'lunch time'
     elif time>=18 and time<=19:
          return 'dinner time'
     else:
          exit()



def convert(time):
     h,m=time.split(':')
     hours=float(h)
     minutes=float(m)
     hours_to_min=hours*60
     minutes_total=hours_to_min + minutes
     time= minutes_total/60
     return time


    # if (hours == 7 and minutes <= 59) or (hours == 8 and minutes == 0):
        # return 'breakfast time'
     #elif (hours == 12 and minutes <= 59) or (hours == 13 and minutes == 0):
      #   return 'lunch time'
     #elif (hours == 18 and minutes <= 59) or (hours == 19 and minutes == 0):
      #   return 'dinner time'
     #else:
       #   return exit()



if __name__ == "__main__":
   print( main())
