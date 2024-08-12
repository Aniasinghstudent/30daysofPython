#a = input('What is your name: ')
#b = input('How old are you? ')

#print(a)
#print(b)

#first_name = 'Ania'
#print(first_name)
#first_name_to_list = list(first_name)
#print(first_name_to_list)

#---------- all above is practice, all below is exercises -----------

#Day 2: 30 Days of python programming

first_name = 'Ania'
last_name = 'Singh'
full_name = 'Ania Singh'
country = 'Norway'
city = 'Stavanger'
age = 14
is_married = False
is_true = "I don't know"
is_light_on = 'No'
fruit, furniture, colour = 'cherry', 'table', 'blue'

# ---- Level 2 ----

print(type('Ania'))
print(type('Singh'))
print(type('Ania Singh'))
print(type('Norway'))
print(type('Stavanger'))
print(type(14))
print(type(False))
print(type("I don't know"))
print(type('No'))

print(len(first_name))
print(len(last_name))
print(len(first_name) - len(last_name))

num_one = 5
num_two = 4
print(num_one+num_two)
print(num_one-num_two)
print(num_one*num_two)
print(num_one/num_two)
remainder = num_one%num_two
print(remainder)
floor_divition = num_one//num_two
print(floor_divition)
exp = num_one**num_two
print(exp)

radius = 30
area_of_circle = 3.14*radius**2
circum_of_circle = 2*radius*3.14

print(area_of_circle)
print(circum_of_circle)

user_radius = int(input('what is the radius of your circle? '))
print(3.14*user_radius**2)

firstname = input('what is your name? ')
lastname = input('what is your last name? ')
country = input('what is your country? ')
age = input('what is your age? ')

user_input = { 
firstname, lastname, country, city
}