# 1. Вычислите 2179. Выведите на экран вычисленное значение.
print(2 * 179)

# 2. Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 179 и 971.
import math

hypo = (179 ** 2 + 971 ** 2) ** 0.5
print(hypo)

import math

ht = 179 ** 2 + 971 ** 2
print(math.sqrt(ht))

# 3. Дано два числа a и b.
# Выведите гипотенузу треугольника с заданными катетами.
import math

a = int(input("Katet A: "))
b = int(input('Katet B: '))

if a <= 0 or b <= 0:
    raise ValueError('Катет не может быть меньше нуля или равен ему')
elif a > 1000 or b > 1000:
    raise ValueError('Введите значение, не превышающее 1000')
else:
    print(round(math.sqrt(a ** 2 + b ** 2), 10))

# 4. Напишите программу, которая приветствует пользователя, выводя слово Hello
name = input('Введите ваше имя: ')
if len(name) > 100:
    raise ValueError("Длина имени превышает лимит символов: 100")
else:
    print("Hello, " + name + "!")

    # 5.Даны два целых числа. Программа должна вывести число 1,
    # если первое число больше второго, число 2,
    # если второе больше первого или число 0, если они равны.
    n1 = int(input('Введите число 1: '))
    n2 = int(input('Введите число 2: '))
    if n1 > n2:
        print(n1)
    elif n2 > n1:
        print(n2)
    else:
        print(0)

    # 6.
    x = int(input('x = '))
    if x > 0:
        print(1)
    elif x < 0:
        print(-1)
    else:
        print(0)

    # 7.
    string = input("Enter: ")
    print(string[2])  # 1
    print(string[-2])  # 2
    print(string[:5])  # 3
    print(string[:-2])  # 4
    print(string[::2])  # 5
    print(string[1::2])  # 6
    print(string[::-1])  # 7
    print(string[::-2])  # 8
    print(len(string))  # 9

    # 8.Дана строка, состоящая из слов, разделенных ровно одним пробелом.
    # Определите, сколько в ней слов.
    # Используйте для решения задачи метод count.
    string = input('Enter: ')
    value = string.count(" ")
    print(value + 1)

    # 9. Считайте со стандартного ввода символ и выведите его код.
    symbol = input('Введите один символ: ')
try:
    print(ord(symbol))
except TypeError:
    print('Введено больше одного символа')

# 10. Считайте со стандартного ввода целое число и выведите ASCII-символ с таким кодом.
# Решите эту задачу с использованием только одной переменной типа int.
number = int(input('Введите ASCII-код: '))
if number < 33 or number > 126:
    raise ValueError('Введите число от 33 до 126 включительно')
else:
    print(chr(number))

# 11. ПОИСК ПОДСТРОКИ
pattern = input("Enter pattern: ")
source = input("Enter source: ")


def IsSubstring(Pattern, Source):
    if Pattern in Source:
        return print("YES")
    else:
        return print("NO")


IsSubstring(pattern, source)
