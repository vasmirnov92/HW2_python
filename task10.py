# Задача 10: 
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2

from random import randint

print('Введите количество монет: ')
monets = input()
monets = int(monets)
# print(monets)

monetStatus = [randint(0, 1) for _ in range(monets)]
print(monetStatus)

orel = 0
reshka = 0
i = 0

while i<monets:
    if monetStatus[i] == 0:
        reshka = reshka + 1
    else:
        orel = orel + 1
    i = i+1

# print(orel)
# print(reshka)

if orel<reshka:
    print(f'Минимальное количество монет, котроые надо перевернуть {orel}')
else:
    print(f'Минимальное количество монет, котроые надо перевернуть {reshka}')


