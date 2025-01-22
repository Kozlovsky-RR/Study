"""Задачи для закрепления курса Python для продвинутых."""


def is_symmetric(matrix: list) -> bool:
    """функция, которая принимает на вход квадратную матрицу и проверяет, является ли она симметричной относительно
        главной диагонали"""
    n = len(matrix)

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
    """функция, которая принимает список строк и возвращает словарь, где ключами являются уникальные слова,
     а значениями — множества индексов строк, в которых эти слова встречаются"""
    my_dict = {}

    for index, string in enumerate(strings):
        for word in string.split():
            my_dict.setdefault(word, set()).add(index)

    return my_dict


strings = [
    "hello world",
    "world of python",
    "hello again"
]
print(words_index_map(strings))


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


def sum_of_moduli(complex_numbers: list) -> float:
    """функция, которая принимает список комплексных чисел и возвращает сумму модулей этих чисел"""
    return sum(map(abs, complex_numbers))

complex_numbers = [complex(3, 4), complex(1, 1), complex(0, 2)]
print(sum_of_moduli(complex_numbers))