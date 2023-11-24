import random
from pprint import pprint

# while - цикл с предусловием
# пока пользовательне введет правильный номер



required_number = 7
user_number = random.randint(0, 10)

while required_number != user_number: # БУДЕТ ВЫПОЛНЯТЬСЯ ПОКА НЕ РАВНО
    user_number = random.randint(0, 10)
    print(f"Пользователь ввел число {user_number}")

iterations_count = 10
i = 0

while i < iterations_count: # Будет выполняться пока числа не станут равны
    i += 1
    print(f"Текущая итерация: {i}")


# for i in rage - цикл с интератором
iterations_count = 10

for i in range(3, iterations_count, 2):
    print(f"Текущая интерация {i}")



# Break / Continue / Else

for i in range(iterations_count):
    if i % 2 == 0:
        continue # ПРЕРЫВАЕТ ЦИКЛ НА ДАННОМ СЛОВЕ
        print("Я никогда не выполнюсь")
    if i > 7:
        break # ВЫХОД ИЗ ЦИКЛА

for i in range(5):
    for j in range(5):
        print(i, j)


# For. Интегрируем списки и словари

users = [
    {"name": "Oleg", "age": 51},
    {"name": "Timur", "age": 16},
    {"name": "Alex", "age": 31},
    {"name": "Alia", "age": 21},
    {"name": "Gala", "age": 52},
]

for user in users:
    print(f"Пользователю {user['name']} {user['age']} лет")


d = {
    "first": 1,
    "second": 2,
    "third": 3
}

for item in d.values():
    print(item)

for item in d.keys():
    print(item)

for item in d.items():
    print(item)

for key, value in d:
    print({key}, {value})




# enumerate - возвращает пары (тндекс и значение)


cities = ["Екатеренбург", "Москва", "Сочи"]

for city in cities:
    print(f"{city} на каком то месте по загрязнению воздуха")

