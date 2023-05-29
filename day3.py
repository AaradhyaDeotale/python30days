#30 days of Python- Day 3
age = 20
height = 1.75
complexno = 2 + 2j

base = float(input("Enter base of the triangle: "))

height = float(input("Enter height of the triangle:  "))

area = 0.5 * base * height

print("The area of triangle is :", area)

radius = float(input("Enter the radius of the circle :"))
circle_area = 3.14*(radius)**2
circum_circle = 2*3.24*radius 
print("Area of the circle is : ", circle_area)
print("Circumference of the circle is : ", circum_circle)

side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

perimeter = side1 + side2 + side3
print("Perimeter of triangle is : ", perimeter)

# y = x^2 + 6x + 9 
a , b , c = 1 , 6 , 9

det = (b^2 - 4*a*c)**(1/2)
print("Determinant is :" ,det)
x1 = (-b + det ) / 2*a
x2 = (-b - det ) / 2*a

print("The two values of the equation y = x^2 + 6x + 9 are:", x1,x2)


