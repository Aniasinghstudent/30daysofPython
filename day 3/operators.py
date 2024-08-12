age = 14
print('age:', age)
height = 162.8
print('height:', height)
complex_variable = 2j+9

user_base = float(input('what is the base of your triangle?: '))
user_height = float(input('what is the height of your triangle?: '))
area = 0.5*user_base*user_height
print('The area of the triangle is:', area)

side_1 = float(input('How long is side a of your triangle?: '))
side_2 = float(input('How long is side b of your triangle?: '))
side_3 = float(input('How long is side c of your triangle?: '))
perimiter = side_1+side_2+side_3
print('The perimiter of the triangle is', perimiter)

length = float(input('What is the length of your rectangle?: '))
width = float(input('What is the width of your rectangle?: '))
rec_area = length*width
rec_perimiter = 2*(length+width)
print('The area of the rectangle is', rec_area)
print('The perimiter of the rectangle is', rec_perimiter)

radius = float(input('What is the radius of your circle?: '))
pi = 3.14
area = pi*radius**2
circum = 2*pi*radius
print('The area is', area)
print('The circumference is', circum)

m=2
b=2
slope_1 = m
y_int = b
x_int = -b/m
print(slope_1)
print(y_int)
print(x_int)

import math

x1, y1, x2, y2 = 2, 2, 6, 10
slope = (y2-y1)/(x2-x1)
print(slope)
e_dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(e_dis)

print(slope_1-slope)

print(len('python') != len('dragon'))
print(('on' in 'dragon') and ('on' in 'python'))
print('jargon' in 'I hope this course is not full of jargon')
print(('on' not in 'python') and ('on' not in 'dragon'))

length = len('python')
print(float(length))
print(str(length))

num = int(input('what is your number '))
if num%2 == 0:
    print('even')
else:
    print('odd')
#the modulus (%) gives out remainders, 
#so when an even number comes it gives 0 cause the remainder of even/2 is 0, 
#it gives out the extra set if number left (without turning it into a float)

facts = 7//3 == int(2.7)
print('7//3 == int(2.7) is', facts)