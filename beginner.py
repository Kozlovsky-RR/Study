'''Задача 1: Реверсирование строки
Напиши функцию, которая принимает строку и возвращает её, но со словами в обратном порядке
Пример:'''

def reverse_words(s: str) -> str:
    return ' '.join(s.split()[::-1])

s = "Hello world from Python"
print(reverse_words(s))

'''Задача 2: Максимальная сумма подмассива
Напиши функцию, которая принимает список чисел и возвращает максимальную сумму подмассива
Пример:'''

def max_subarray_sum(nums: list) -> int:
    max_sum = 0
    current_sum = 0


    for i in range(len(nums)):
        current_sum = current_sum + nums[i]

        if current_sum < 0:
            current_sum = 0

        elif current_sum > max_sum:
            max_sum = current_sum


    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(nums))

'''Задача 3: Частота символов
Напиши функцию, которая принимает строку и возвращает словарь, где ключами являются символы, а значениями — их частота в строке
Пример:'''

def char_frequency(s: str) -> dict:
    my_dict = {}

    for i in s:
        my_dict.setdefault(i, 0)
        my_dict[i] += 1

    return my_dict

s = "abracadabra"
print(char_frequency(s))

'''Задача 4: Проверка анаграммы
Напиши функцию, которая принимает две строки и проверяет, являются ли они анаграммами (т.е. состоят ли они из одних и тех же символов в одинаковом количестве)
Пример:'''

def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))
