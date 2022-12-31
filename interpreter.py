#def math_i(x,y,z):
num = input('Expression:')
x,y,z = num.split()
num1=int(x)
num2=int(z)
match y:
    case '+':
        add=num1+num2
        print('%.1f'% add)

    case '-':
        sub=num1-num2
        print('%.1f'% sub)

    case '*':
        prod=num1*num2
        print('%.1f'% prod)

    case '/':
        div=num1/num2
        print('%.1f'% div)