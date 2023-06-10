"""
Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные
(без повтора) элементы исходного списка.
*Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков

"""


def uniq(numbers: list) -> list:
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result


def uniq2(numbers: list) -> list:
    return list(set(numbers))


"""
Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
целое положительное число
вещественное положительное или отрицательное число
строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
строку в верхнем регистре в остальных случаях
"""


def reformat(text: str) -> (int, float, str):
    # result = None
    if ("." in text or (text.count("-") and text.index("-") == 0)) and text.replace(".", "").replace("-", "").isdigit():
        result = float(text)
    elif text.isdigit():
        result = int(text)
    elif text.lower() != text:
        result = text.lower()
    else:
        result = text.upper()

    return result


"""
Создайте вручную кортеж содержащий элементы разных типов. 
Получите из него словарь списков, где 
ключ - тип элемента,
значение - список элементов данного типа
"""


def get_type_dict(corteg: tuple) -> dict:
    result = {}
    for i in corteg:
        result.setdefault(type(i), []).append(i)
    return result


"""
Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
"""


def double_count(my_list: list) -> list:
    return list(filter(lambda x: my_list.count(x) != 2, my_list))


"""
Создайте вручную список с повторяющимися целыми числами. 
Сформируйте список с порядковыми номерами нечётных элементов исходного списка. 
Нумерация начинается с единицы.
"""


def odd_index(my_lst: list[int]) -> list:
    return [i for i, j in filter(lambda x: x[1] % 2 != 0, enumerate(my_lst, 1))]


"""
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
Строки нумеруются начиная с единицы
Слова выводятся отсортированными согласно кодировки Unicode
Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки
"""


def num_of_words(text: str):
    result = sorted(text.split())
    [print(f"{i} {word:>{len(max(result, key=len))}}") for i, word in enumerate(result, 1)]