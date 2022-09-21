'''4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     периметр квадрата, площадь квадрата и диагональ квадрата'''
from math import sqrt
from functools import reduce


def measures(side):
    return (side * 4, side * side, sqrt(side))


print(measures(5))

'''4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов 
и выводит их построчно в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35 
	position: web developer'''


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


'''4.3. Используя лямбда-выражение, из списка 
my_list = [20, -3, 15, 2, -1, -21] 
создайте новый список, содержащий только положительные числа'''


my_list = [20, -3, 15, 2, -1, -21]
print(list(filter(lambda x: x > 0, my_list)))

'''4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке '''

print(reduce(lambda x, y: x * y, my_list))

