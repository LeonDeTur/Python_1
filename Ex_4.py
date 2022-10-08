# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Enter № of quarter (1, 2, 3 or 4): "))

if quarter == 1:
    print ("Possible coordinates are from (1;1) to (infinity;infinity)")
elif quarter == 2:
    print ("Possible coordinates are from (-1;1) to (-infinity;infinity)")
elif quarter == 3:
    print ("Possible coordinates are from (-1;-1) to (-infinity;-infinity)")
else:
    print ("Possible coordinates are from (1;-1) to (infinity;-infinity)")