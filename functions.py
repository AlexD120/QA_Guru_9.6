# Объявление функции
from operator import itemgetter
from pprint import pprint


def my_func():
    print("Мы вызвали функцию")

my_func()

# ФУНКЦИЯ С ПОЗИЦИОННЫМИ АРГУМЕНТАМИ

def sum_numbers(a: int, b: int):
    print(a + b)

sum_numbers("ds", "dss")
sum_numbers(15, 80)
sum_numbers(10, 5)

# ФУНКЦИЯ С ИМЕНОВАННЫМИ АРГУМЕНТАМИ

sum_numbers(a=15, b=35)

# ФУНКЦИЯ С АРГУМЕНТАМИ ПО УМОЛЧАНИЮ

def multiply(n, mult: int = 2):
    print(n * mult)

multiply(10)
multiply(10, mult=5)



# ВОЗВРАЩАЕМ ЗНАЧЕНИЕ

def sum(a: int, b: int):
    return a + b

n = sum(55, 45)
print(n)

# ВОЗВРАЩАЕМ НЕСКОЛЬКО ЗНАЧНИЙ

def return_tuple():
    return 1, 2, 3

t = return_tuple()
print(t)

t1, t2, t3 = return_tuple()
print(t1, t2, t3)

# t1, t2 = return_tuple()
# print(t1, t2)

t1, *t2 = return_tuple()
print(t1, t2)

t1,t2, *t3 = return_tuple()
print(t1, t2, t3)


# ПЕРЕМЕННОЕ КОЛИЧЕСТВО АРГУМЕНТОВ НА ПРИМЕРЕ print

def custom_print(*args): #МОЖНО ПЕРЕДАТЬ СКОЛЬКО УГОДНО АРГУМЕНТОВ
    # for arg in args:
    #     print(arg)
    print(args)
    print(*args)

custom_print(1, 2, 3, 4, 5, 6)

# ПЕРЕМЕННОЕ КОЛИЧЕСТВО ИМЕНОВАННЫХ АРГУМЕНТОВ

def custom_named_print(*args, **kwargs):
    print(args, kwargs)
    print(*args, **kwargs)

custom_named_print(1, 2, 3, 4, 5, end="!\n", sep=" | ")

# ОБЛАСТЬ ВИДИМОСТИ ПЕРЕМЕННЫХ

v = 123

def my_awersome_func():
    v =  456
    print(v)

print(v)
my_awersome_func()
print(v)

# ФУНКЦИЯ - ТОЖЕ ОБЪЕКТ

p = print

p(1, 2, 3, 4, 5)

users = [
    {"name": "Oleg", "age": 51},
    {"name": "Timur", "age": 16},
    {"name": "Alex", "age": 31},
    {"name": "Alia", "age": 21},
    {"name": "Gala", "age": 52},
]

def get_age(user):
    return user["age"]


users.sort(key=get_age, reverse=True) # СОРТИРУЕМ СПИСОК ПО ВОЗРАСТУ

users.sort(key=lambda user: user["age"]) # Лямда функции

users.sort(key=itemgetter('age')) #Функция возвращающая функцию

pprint(users)
