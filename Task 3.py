# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

import random


array = []
for i in range(20):
    array.append(random.randint(1, 5))
print(f'Array : {array}')

new_array = []
[new_array.append(i) for i in array if i not in new_array]
new_array.sort()
print(f'New array : {new_array}')
