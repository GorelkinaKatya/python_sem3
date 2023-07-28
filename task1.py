from random import randint
list_1 = [randint(1, 5) for i in range(0, 10)]
print(list_1)
k = int(input('Введите число: '))

count = 0

for i in list_1:
    if i == k:
        count += 1

print(count)