# Задача 1
# Напишите функцию get_squares_sum(arr), которая принимает в качестве аргумента
# список из целых чисел, а возвращает одно целое число - сумму квадратов этих чисел.

def get_squares_sum(arr):
    return sum(x ** 2 for x in arr)
# Примеры использования
print(get_squares_sum([1, 2, 3]))  # Вывод: 14
print(get_squares_sum([4, 4]))     # Вывод: 32
print(get_squares_sum([-1, -2]))   # Вывод: 5