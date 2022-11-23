name = 'Vandana'

if len(name) < 3:
    print('name must be at least 3 characters')
elif len(name) > 50:
    print('name can be of maximum 50 characters')
else:
    print('name looks good')


weight = input('Enter your weight: ')
unit  = input('(L)bs or K(g): ')

if unit == 'l' or unit == 'L':
    weight = int(weight) * 0.45
    print(f'you are {weight} kilos')
elif unit == 'k' or unit == 'K':
    weight = int(weight) / 0.45
    print(f'you are {weight} pounds')