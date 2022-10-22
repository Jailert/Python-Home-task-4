# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input("Enter number: "))
i = 2
array = []
while i <= num:
    if num % i == 0:
        array.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Our list: {array}")
