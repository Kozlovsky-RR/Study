from collections import Counter


"""Задачи для закрепления курса Python для начинающих."""


def reverse_words(s: str) -> str:
    """функция, которая принимает строку и возвращает её, но со словами в обратном порядке"""
    return ' '.join(s.split()[::-1])


s = "Hello world from Python"
print(reverse_words(s))
'''Python from world Hello'''



def max_subarray_sum(nums: list) -> int:
    """функция, которая принимает список чисел и возвращает максимальную сумму подмассива"""
    max_so_far = float("-inf")
    current_sum = 0

    for i in nums:
        current_sum = max(i, current_sum + i)
        max_so_far = max(max_so_far, current_sum)

    return max_so_far


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))


def char_frequency(s: str) -> dict:
    return dict(Counter(s))


s = "abracadabra"
print(char_frequency(s))


def are_anagrams(s1: str, s2: str) -> bool:
    """функция, которая принимает две строки и проверяет, являются ли они анаграммами"""
    return Counter(s1) == Counter(s2)


s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))
