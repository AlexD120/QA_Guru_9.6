# Boolean 3 состояния

b = bool

t = True
f = False
n = None

# if / else / elif

if True:
    print("Я выполняюсь!")

if False:
    print("Я никогда не выполнюсь!")


code = 900

if 200 <= code <= 400:
    print('Проверка проведена, хороший ответ')
elif 400 <= code <= 600:
    print('Плохой код ответа')
else:
    print('Какой-то странный код ответа')

# Пустые объекты - false

user_list = []
if user_list == []:
    pass


item_count = 0
if item_count == 0:
    pass

print(bool(100))
print(bool(-100))
print(bool(0))

print(bool("asd"))
print(bool(""))

print(bool([]))
print(bool([1, 2, 3]))
print(bool(False))