"""Задачи для закрепления курса Python для продвинутых."""
from collections import defaultdict


def is_symmetric(matrix: list) -> bool or str:
    """Функция, которая принимает на вход квадратную матрицу и проверяет, является ли она симметричной относительно
        главной диагонали."""
    n = len(matrix)
    if len(matrix[0]) != n:
        return "Матрица не квадратная"

    for i in range(n):
        for j in range(n):
            if j > i:
                if matrix[i][j] != matrix[j][i]:
                    return False

    return True


matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
print(is_symmetric(matrix))


def words_index_map(strings: list) -> dict:
    """Функция, которая принимает список строк и возвращает словарь, где ключами являются уникальные слова,
     а значениями — множества индексов строк, в которых эти слова встречаются."""

    d = defaultdict(set)
    for k, v in enumerate(strings):
        for j in v.split():
            d[j].add(k)

    return dict(d)


strings = [
    "hello world",
    "world of python",
    "hello again"
]
print(words_index_map(strings))


def clean_file(input_file: str, output_file: str) -> None:
    """Программа, которая читает текстовый файл, удаляет из него все пустые строки и строки,
       состоящие только из пробелов, а затем записывает результат в новый файл."""
    with open(input_file, 'r', encoding='utf-8') as file1:
        lst = [i.lstrip() for i in file1.readlines()]
        lst = filter(lambda x: len(x) > 0, lst)

    with open(output_file, 'w', encoding='utf-8') as file2:
        file2.writelines(lst)



input_file = "input.txt"
output_file = "output.txt"
clean_file(input_file, output_file)


def sum_of_moduli(complex_numbers: list) -> float:
    """Функция, которая принимает список комплексных чисел и возвращает сумму модулей этих чисел."""
    return sum(map(abs, complex_numbers))

complex_numbers = [complex(3, 4), complex(1, 1), complex(0, 2)]
print(sum_of_moduli(complex_numbers))