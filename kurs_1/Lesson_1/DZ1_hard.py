__author__ = 'Makarkin Maxim Boricovich'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)

a = 1000000 print('a =', a)0

print(bool(a) == bool(a**2))
print(bool(a) == bool(a*2))
print(a > 999999)
print('Значение не менялось. Любое число > 999999. a =', a)