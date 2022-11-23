# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
def range_of_point(n):
    match n:
        case 1:
            return "X > 0 and Y > 0"
        case 2:
            return "X < 0 and Y > 0"
        case 3:
            return "X < 0 and Y < 0"
        case 4:
            return "X > 0 and Y < 0"
        case _:
            return "Не верно введен номер четверти"

try:
    n=int(input("Введи номер четверти: "))
    a=range_of_point(n)
    print(a)
except:
    print("Ты ошибся. Вводить надо числа!")




