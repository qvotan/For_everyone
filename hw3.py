''' 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd'].
 Распечатайте значения 1, 2, 3'''

my_list = ['a', 'b', [1, 2, 3], 'd']
# print('\n'.join(map(str, my_list)))

print(*my_list, sep=" ")
'''3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
    - получите сумму всех чисел,
    - распечатайте все строки, где есть буква 'a'''

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
print(sum([x for x in list_1 if isinstance(x, int)]))
print([x for x in list_1 if isinstance(x, str) and 'a' in x])

'''3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж'''

list_2 = ['cat', 'dog', 'horse', 'cow']
list_21 = tuple(list_2)
print(type(list_21))

'''3.4. Напишите программу, которая определяет, какая семья больше. 
      1) Программа имеет два input() - например, family_1, family_2. 
      2) Членов семьи нужно перечислить через запятую. 
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal') '''

family_1 = input().split(',')
family_2 = input().split(',')
if len(family_1) == len(family_2):
    print("Equal")
elif len(family_1) > len(family_2):
    print('family_1')
else:
    print('family_2')

'''3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. 
В значения можете передать информацию о вашем любимом фильме. 
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение'''

my_film = {'title': 'Inception.', 'actor': 'Leo DiCaprio',
           'genre': 'thriller', 'director': 'Christopher Nolan'}
print(my_film.keys())
print(my_film.values())
print(my_film.items())

'''3.6. Найдите сумму всех значений в словаре 
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}'''

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum([value for value in my_dictionary.values()]))

'''3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1] '''

my_list4 = [1, 2, 3, 4, 5, 3, 2, 1]
print(set(my_list4))

'''3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'},
                            set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга '''

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1 & set2)
print(set1 ^ set2)
print(set1 < set2)
