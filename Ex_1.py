# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print("Please, enter integer number from 1 to 7 to get the name of the week day.")
week_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
num = round(int(input()))
if 1 <= num <= 5:
    print("It's " + week_day[num-1])
elif 6 <= num <=7:
    print("It's " + week_day[num-1])
else:
    print("There is only 7 days in week. Please, restart the programm and enter integer number from 1 to 7.")
