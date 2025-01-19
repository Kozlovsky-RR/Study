"""Задача 1: Проверка матрицы на симметричность"""


def is_symmetric(matrix: list) -> bool:
    """функция, которая принимает на вход квадратную матрицу и проверяет, является ли она симметричной относительно
        главной диагонали"""
    n = len(matrix)


    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True


matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
print(is_symmetric(matrix))


"""Задача 2: Словари и множества"""


def words_index_map(strings: list) -> dict:
    """функция, которая принимает список строк и возвращает словарь, где ключами являются уникальные слова,
     а значениями — множества индексов строк, в которых эти слова встречаются"""
    my_dict = {}

    for i in range(len(strings)):
        for j in strings[i].split():

            my_dict[j] = my_dict.get(j, set())
            my_dict[j].add(i)

    return my_dict



strings = [
    "hello world",
    "world of python",
    "hello again"
]
print(words_index_map(strings))


"""Задача 3: Работа с файлами"""

def clean_file(input_file: str, output_file: str) -> None:
    """программа, которая читает текстовый файл, удаляет из него все пустые строки и строки, состоящие только из пробелов,
     а затем записывает результат в новый файл"""
    with open(input_file, 'r', encoding='utf-8') as file1:
        without_spaces = filter(lambda x: len(x) > 0, [i.lstrip() for i in file1.readlines()])

    with open(output_file, 'w', encoding='utf-8') as file2:
        file2.writelines(without_spaces)


input_file = "input.txt"
output_file = "output.txt"
clean_file(input_file, output_file)

"""Задача 4: Комплексные числа"""


def sum_of_moduli(complex_numbers: list) -> float:
    """функция, которая принимает список комплексных чисел и возвращает сумму модулей этих чисел"""
    return sum(map(abs, complex_numbers))

complex_numbers = [complex(3, 4), complex(1, 1), complex(0, 2)]
print(sum_of_moduli(complex_numbers))