"""Задачи для закрепления курса Python для начинающих."""


from collections import Counter
from typing import Union


def reverse_words(s: str) -> str:
    """Функция, которая принимает строку и возвращает её, но со словами в обратном порядке."""
    if len(s) == 0:
        return "Вы не ввели строку"

    return ' '.join(s.split()[::-1])


s: str = "Hello world from Python"
print(reverse_words(s))


def max_subarray_sum(nums: list[int]) -> Union[int, list]:
    """Функция, которая принимает список чисел и возвращает максимальную сумму подмассива."""
    if len(nums) == 0:
        return nums

    max_so_far: float = float("-inf")
    current_sum: int = 0

    for i in nums:
        current_sum: int = max(i, current_sum + i)
        max_so_far: int = max(max_so_far, current_sum)

    return max_so_far


nums: list[int] = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))


def char_frequency(s: str) -> dict[str, int]:
    """Функция, которая принимает строку, и возвращает словарь,
     где ключами являются символы, а значениями их частота в строке."""
    return dict(Counter(s))


s: str = "abracadabra"
print(char_frequency(s))


def are_anagrams(s1: str, s2: str) -> bool:
    """Функция, которая принимает две строки и проверяет, являются ли они анаграммами."""
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


s1: str = "listen"
s2: str = "silent"
print(are_anagrams(s1, s2))
