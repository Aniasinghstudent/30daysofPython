num = int(input('enter your age: '))
if num > 18:
    print('You can drive!')

elif num < 18:
    sum = 18-num
    print('you have to wait' , sum ,'years till you can drive')

elif num == 18:
    print('You can drive!')

age = int(input('Enter your age: '))

if age < 14:
    sum = 14-age
    print('I am', sum, 'years older than you')

elif age > 14:
    sum = age-14
    print('You are', sum, 'years older than me')

elif age == 14:
    print('You are just as old as me!')

a = int(input('Enter a number: '))
b = int(input('Enter another number: '))

if a == b:
    print(a, 'and', b, 'are equal')
elif a > b:
    print(a, 'is greater than', b)
elif a < b:
    print(b, 'is greater than', a)

scr = int(input('Type in your score: '))
if 100 >= scr >= 90:
    print('You got an A!')
elif 89 >= scr >= 70:
    print('You got a B!')
elif 69 >= scr >= 60:
    print('You got a C!')
elif 59 >= scr >= 50:
    print('You got a D!')
elif 49 >= scr >= 0:
    print('You got a F!')

month = input('Enter the month (uppercase first letter): ')
if month in ('September, October, November'):
    print('The season is Autumn')
elif month in ('December, January, February'):
    print('The season is Winter')
elif month in ('March, April, May'):
    print('The season is Spring')
elif month in ('June, July, August'):
    print('The season is Summer')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('What fruit do you want to add to the list? ')
if fruit in fruits:
    print('That fruit already exists in the list.')
elif fruits.append:(fruit), print('Your fruit has been added to the list!')

person={
    'first_name': 'Ania',
    'last_name': 'Singh',
    'age': 14,
    'country': 'Norway',
    'is_marred': False,
    'skills': ['Python'],
    'address': {
        'street': 'Perfect Blv',
        'zipcode': '10101'
    }
    }
if 'skills' in person:
    print(person['skills'])
    if 'Python' in 'skills':
        print('skills')
