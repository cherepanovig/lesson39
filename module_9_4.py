# Домашнее задание по теме "Создание функций на лету"
# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.

first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda-функция:
result1 = list(map(lambda a, b: a == b, first, second))
print(result1)

# Списочная сборка
result2 = [first[i] == second[i] for i in range(min(len(first), len(second)))]
# Так как нам можно перебирать по индексам только до длины более короткой строки, то используем
# range(min(len(first), len(second)))
print(result2)


# Замыкание:

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:  # Открываем файл на запись
            for i in data_set:  # Перебираем элементы data_set
                file.write(f'{i}\n')  # Записываем элементы построчно
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:

from random import choice
class MysticBall:

    def __init__(self, *words):
        self.words = list(words)  # Преобразуем передаваемые строки в список, чтобы choice выбирала из списка

    def __call__(self):
        random_word = choice(self.words)
        return random_word


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Может быть', 'Вряд ли')
print(first_ball()) # вызываем объект класса first_ball как функцию благодаря __call__(self)
print(first_ball())
print(first_ball())
print(first_ball())
