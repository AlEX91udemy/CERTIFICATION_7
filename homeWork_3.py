# Задача 3
# Программист Геннадий очень любит не только писать код, но и читать умные книжки!
# Так, сидя за обеденным перерывом, он наткнулся на статью в интернете, в которой
# говорилось, что если выписать первые 5 самых часто встречающихся букв в книге (не
# считая пробелов), то получится слово, по которому можно понять ее смысл. Геннадий
# очень хочет, чтобы вы проверили эту теорию! Ваша задача написать программу,
# которая выводит слово, составленное из 5 букв с наибольшей частотой вхождения в
# текст. Буквы в этом слове должны быть отсортированы по убыванию количества
# вхождений в текст.

from collections import Counter


def find_most_frequent_letters(text):
    letters = [char.lower() for char in text if char.isalpha()]
    letter_counts = Counter(letters)
    most_common_letters = letter_counts.most_common(5)
    sorted_letters = sorted(most_common_letters, key=lambda x: x[1], reverse=True)
    result_word = ''.join(letter for letter, _ in sorted_letters)

    return result_word


# Пример использования
input_text = "шашки шакша каша шаверма"
result = find_most_frequent_letters(input_text)
print(result)  # Выведет "ашкив"
