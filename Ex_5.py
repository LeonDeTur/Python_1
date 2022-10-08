# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt

xA = int(input("Enter first coordinate of first point(xA): "))
yA = int(input("Enter second coordinate of first point(yA): "))
xB = int(input("Enter first coordinate of second point(xB): "))
yB = int(input("Enter second coordinate of second point(yB): "))
result = sqrt((xA -xB)**2 + (yA - yB)**2)
print(f"Distance between points is equal: {result}")