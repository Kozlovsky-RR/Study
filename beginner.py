"""Задачи для закрепления курса Python для начинающих."""
from collections import Counter


def reverse_words(s: str) -> str:
    """Функция, которая принимает строку и возвращает её, но со словами в обратном порядке."""
    if len(s) == 0:
        return "Вы не ввели строку"

    return ' '.join(s.split()[::-1])


s = "Hello world from Python"
print(reverse_words(s))


def max_subarray_sum(nums: list) -> int or list:
    """Функция, которая принимает список чисел и возвращает максимальную сумму подмассива."""
    if len(nums) == 0:
        return nums

    max_so_far = float("-inf")
    current_sum = 0

    for i in nums:
        current_sum = max(i, current_sum + i)
        max_so_far = max(max_so_far, current_sum)

    return max_so_far


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))


def char_frequency(s: str) -> dict:
    """Функция, которая принимает строку, и возвращает словарь,
     где ключами являются символы, а значениями их частота в строке."""
    return dict(Counter(s))


s = "abracadabra"
print(char_frequency(s))


def are_anagrams(s1: str, s2: str) -> bool:
    """Функция, которая принимает две строки и проверяет, являются ли они анаграммами."""
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))
