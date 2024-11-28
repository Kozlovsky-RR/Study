from collections import Counter


"""Задача 1: Реверсирование строки"""


def reverse_words(s: str) -> str:
    """функция, которая принимает строку и возвращает её, но со словами в обратном порядке"""
    return ' '.join(s.split()[::-1])


s = "Hello world from Python"
print(reverse_words(s))
'''Python from world Hello'''


'''Задача 2: Максимальная сумма подмассива'''


def max_subarray_sum(nums: list) -> int:
    """функция, которая принимает список чисел и возвращает максимальную сумму подмассива"""
    max_sum = 0
    current_sum = 0

    for i in range(len(nums)):
        current_sum = current_sum + nums[i]

        if current_sum < 0:
            current_sum = 0

        elif current_sum > max_sum:
            max_sum = current_sum

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))

'''Задача 3: Частота символов'''


def char_frequency(s: str) -> dict:
    return dict(Counter(s))


s = "abracadabra"
print(char_frequency(s))

'''Задача 4: Проверка анаграммы'''


def are_anagrams(s1: str, s2: str) -> bool:
    """функция, которая принимает две строки и проверяет, являются ли они анаграммами"""
    return Counter(s1) == Counter(s2)


s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))
