# Задана натуральная степень k
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("Enter k = "))


def fillrandom():
    return random.randint(0, 101)


def polynomial(k):
    lst = [fillrandom() for i in range(k+1)]
    return lst


def write_file(st):
    with open('Task 4.txt', 'w') as data:
        data.write(st)


def create_string(sp):
    lst = sp[::-1]
    write = ''
    if len(lst) < 1:
        write = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                write += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    write += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                write += f'{lst[i]}x'
                if lst[i+1] != 0:
                    write += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                write += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                write += ' = 0'
    return write


koef = polynomial(k)
write_file(create_string(koef))
