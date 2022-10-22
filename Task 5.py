# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random


def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)


def fileng2random():
    return random.randint(0, 101)


def polynomial(k):
    lst = [fileng2random() for i in range(k+1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


def pow_poly(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def k_poly(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    leng = len(st)

    if pow_poly(st[-1]) == -1:
        lst.append(int(st[-1]))
        leng -= 1

    pow = 1
    indx = leng - 1
    while indx >= 0:
        if pow_poly(st[indx]) != -1 and pow_poly(st[indx]) == pow:
            lst.append(k_poly(st[indx]))
            indx -= 1
            pow += 1
        else:
            lst.append(0)
            pow += 1

    return lst


k1 = int(input("Enter k1 = "))
k2 = int(input("Enter k2 = "))
koef1 = polynomial(k1)
koef2 = polynomial(k2)
write_file("Task 5_1.txt", create_str(koef1))
write_file("Task 5_2.txt", create_str(koef2))


with open('Task 5_1.txt', 'r') as data:
    st1 = data.readlines()
with open('Task 5_2.txt', 'r') as data:
    st2 = data.readlines()

lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
leng2 = len(lst1)
if len(lst1) > len(lst2):
    leng2 = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(leng2)]
if len(lst1) > len(lst2):
    leng1 = len(lst1)
    for i in range(leng2, leng1):
        lst_new.append(lst1[i])
else:
    leng1 = len(lst2)
    for i in range(leng2, leng1):
        lst_new.append(lst2[i])
write_file("Task 5 result", create_str(lst_new))
with open('Task 5 result', 'r') as data:
    st3 = data.readlines()
print(f"Result Polynomial {st3}")
