# 3.1
my_list = ['a', 'b', [1, 2, 3], 'd']
[[print(i) for i in x] for x in my_list if isinstance(x, list)]

# 3.2
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
print(sum([x for x in list_1 if isinstance(x, int)]))
[print(x) for x in list_1 if isinstance(x, str) and x.find('a') != -1]

# 3.3
animals = ['cat', 'dog', 'horse', 'cow']
print(tuple(animals))

# 3.4
family_1 = input('Введите членов первой семьи через запятую\n')
family_1_arr = family_1.split(',')
family_2 = input('Введите членов второй семьи через запятую\n')
family_2_arr = family_2.split(',')
print('Equal') if len(family_1_arr) == len(family_2_arr) else print(family_1_arr) if len(family_1_arr) > len(family_2_arr) else print(family_2_arr)

# 3.5
film = {'title': 'House M.D.', 'director': 'David Shore', 'year': '2004–2012', 'budget': 'unknown', 'main_actor': 'Hugh Laurie', 'slogan': 'Genius has side effects'}
print(film.keys())
print(film.values())
print(film.items())

# 3.6
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum([value for value in my_dictionary.values()]))

# 3.7
print(list(set([1, 2, 3, 4, 5, 3, 2, 1])))

# 3.8
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1 & set2)
print(set1 ^ set2)
print(set1 < set2, set2 < set1)
