# Three sides of the triangle a, b and c are provided by the user

a = float(input('Enter First Side:'))
b = float(input('Enter Second Side:'))
c = float(input('Enter Third Side:'))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)