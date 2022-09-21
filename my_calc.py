'''4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие
        базовые арифметические вычисления.
     Примените эти функции в качестве методов в другом файле. '''


def sum_(a, b):
    return a + b


def sub_(a, b):
    return a - b


def mul_(a, b):
    return a * b


def div_(a, b):
    try:
        return a / b
    except ZeroDivisionError as divzero:
        return repr(divzero)


def pow_(a, b):
    return a ** b
