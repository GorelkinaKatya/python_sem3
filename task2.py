from random import randint
list_1 = [randint(1, 5) for i in range(0, 10)]
print(list_1)
k = int(input('Введите число: '))

# diff = float('inf')
# number = 0

# for i in list_1:
#     if abs(k - list_1[i]) <= diff:
#         diff = abs(k - list_1[i])
#         number = list_1[i]

# print(number)

diff = float('inf')
number = 0

for i in list_1:
    if abs(k - i) <= diff:
        diff = abs(k - i)
        number = i

print(number)
