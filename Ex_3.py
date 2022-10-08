# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Enter first coordinate: "))
y = int(input("Enter second coordinate: "))

if x > 0 and y > 0:
    print("Point is in first quarter")
elif x < 0 and y > 0:
    print("Point is in second quarter")
elif x < 0 and y < 0:
    print("Point is in third quarter")
else:
    print("Point is in forth quarter")