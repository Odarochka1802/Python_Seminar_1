# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
try:
    match n := int(input("Введите цифру обозначающую день недели: ")):
        case 1 | 2 | 3 | 4 | 5:
            print("нет")
        case 6 | 7:
            print("да")
        case _:
            print("Введено число больше или меньше допустимого")
except:
    print("Введено не числовое значение")
