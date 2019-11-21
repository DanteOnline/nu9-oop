"""
Приведенеие типов
"""

greeting = ''
greeting = 'Hello, World!'

# Пустая это строка или нет
if len(greeting) > 0:
    print('не пустая')

"""
True - истина
непустая строка
непустой список
непустой кортеж
число != 0
непустой словарь
непустое множество
"""

"""
False
пустоя строка
None
пустой список
пустой кортеж
пустое множество
пустой словарь
0
"""

if greeting:
    print('не пустая')

true_obj = 'abc'
true_obj = [1, 2, 3]
true_obj = {'a'}
true_obj = {'a': 1}
true_obj = 10

false_obj = ''
false_obj = []
false_obj = set()
false_obj = dict()
false_obj = 0
false_obj = None

if not false_obj:
    pass
