#
# x = int(input("enter a number : "))
#
# if (type(x) == int):
#     print("this is a number")
# else:
#     print(f" {x} is not a number")
from time import process_time_ns

# num1 = int(input("input num 1 : "))
# num2 = int(input("input num 2 : "))
#
# sum = num1 + num2
# dif = num1 - num2
# prod = num1 * num2
# quot = num1 / num2
# modulo = num1 % num2
#
# print(f"The sum of num1,num2 is {sum}")
# print(f"The difference of num1,num2 is {dif}")
# print(f"The product of num1,num2 is {prod}")
# print(f"The quotient of num1,num2 is {quot:2f}")
# print(f"The modulo of num1,num2 is {modulo}")

# c = float(input("enter celsius : "))
#
# f = (c * (9/5)) + 32
#
# print(f"Fahrenheit : {f:.2f}")

# import math as m
#
# s = 10
# l = 8
# w = 10
# b = 5
# h = 8
# r = 15
#
# areaSquare = s**2
# areaRectangle = l * w
# areaTriangle = (1/2) * b * h
# areaCircle = m.pi * r**2
#
# print(f"Area of Square {areaSquare}")
# print(f"Area of Rectangle {areaRectangle}")
# print(f"Area of Triangle {areaTriangle:.2f}")
# print(f"Area of Circle {areaCircle:.2f}")

x = int(input("enter x axis : "))
y = int(input("enter y axis : "))

if x > 0 and y > 0:
    print(f"{x} and {y} is in Quadrant 1")

elif x > 0 and y < 0:
    print(f"{x} and {y} is in Quadrant 4")

elif x < 0 and y < 0:
    print(f"{x} and {y} is in Quadrant 3")

elif x < 0 and y > 0:
    print(f"{x} and {y} is in Quadrant 2")

elif x == 0 and y == 0:
    print("origin")

elif x == 0 and y > 0:
    print("Positive Y axis")

elif x == 0 and y < 0:
    print("Negative Y axis")

elif x > 0 and y == 0:
    print("Positive X axis")

elif x < 0 and y == 0:
    print("Negative X axis")

else:
    print("please enter a number")





# name = "Markraymund Dumaog"
#
# for i in name:
