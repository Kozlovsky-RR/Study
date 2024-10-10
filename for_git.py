# Задача 1: Реверсирование строки
# Напиши функцию, которая принимает строку и возвращает её, но со словами в обратном порядке
# Пример:

def reverse_words(s: str) -> str:
    return ' '.join(s.split()[::-1])
#Тест
s = "Hello world from Python"
print(reverse_words(s))  # "Python from world Hello"

#Задача 2: Максимальная сумма подмассива
# Напиши функцию, которая принимает список чисел и возвращает максимальную сумму подмассива
# Пример:

def max_subarray_sum(nums: list) -> int:
    max_sum = 0
    max_now = 0


    for i in range(len(nums)):
        max_now = max_now + nums[i]

        if max_now < 0:
            max_now = 0

        elif max_now > max_sum:
            max_sum = max_now


    return max_sum
# Тест
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(nums))  # 6 (подмассив [4,−1,2,1])

# Задача 3: Частота символов
# Напиши функцию, которая принимает строку и возвращает словарь, где ключами являются символы, а значениями — их частота в строке
# Пример:

def char_frequency(s: str) -> dict:
    my_dict = {}

    for i in s:
        my_dict.setdefault(i, 0)
        my_dict[i] += 1

    return my_dict

    # Второй вариант

    # my_dict = {}
    #
    # for i in set(s):
    #     my_dict[i] = s.count(i)
    #
    # return my_dict
# Тест
s = "abracadabra"
print(char_frequency(s))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

# Задача 4: Проверка анаграммы
# Напиши функцию, которая принимает две строки и проверяет, являются ли они анаграммами (т.е. состоят ли они из одних и тех же символов в одинаковом количестве)
# Пример:

def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

#Тест
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  # True


# Задача 1: Проверка матрицы на симметричность
# Напиши функцию, которая принимает на вход квадратную матрицу и проверяет, является ли она симметричной относительно главной диагонали
# Пример:

def is_symmetric(matrix: list) -> bool:
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Тест
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
print(is_symmetric(matrix))  # True


# Задача 2: Словари и множества
# Напиши функцию, которая принимает список строк и возвращает словарь, где ключами являются уникальные слова, а значениями — множества индексов строк, в которых эти слова встречаются
# Пример:

def words_index_map(strings: list) -> dict:
    my_dict = {}

    for i in range(len(strings)):
        for j in strings[i].split():
            my_dict[j] = my_dict.get(j, set())
            my_dict[j].add(i)

    return my_dict


# Тест
strings = [
    "hello world",
    "world of python",
    "hello again"
]
print(words_index_map(strings))
# {'hello': {0, 2}, 'world': {0, 1}, 'of': {1}, 'python': {1}, 'again': {2}}

# Задача 3: Работа с файлами
# Напиши программу, которая читает текстовый файл, удаляет из него все пустые строки и строки, состоящие только из пробелов, а затем записывает результат в новый файл
# Пример:

def clean_file(input_file: str, output_file: str) -> None:
    with open(input_file, 'r', encoding='utf-8') as file1:
        without_spaces = list(filter(lambda x: len(x) > 0, [i.lstrip() for i in file1.readlines()]))

    with open(output_file, 'w', encoding='utf-8') as file2:
        file2.writelines(without_spaces)

# Тест
input_file = "input.txt"
output_file = "output.txt"
clean_file(input_file, output_file)

# Задача 4: Комплексные числа
# Напиши функцию, которая принимает список комплексных чисел и возвращает сумму модулей этих чисел
# Пример:

def sum_of_moduli(complex_numbers: list) -> float:
    return sum(map(abs, complex_numbers))
# Тест
complex_numbers = [complex(3, 4), complex(1, 1), complex(0, 2)]
print(sum_of_moduli(complex_numbers))  # 8.4
