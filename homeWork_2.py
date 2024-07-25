# Задача 2
# Учитель информатики Валерий очень любит своих студентов, поэтому Валерий решил
# выставлять оценку за год, учитывая только четные оценки ученика. Таким образом,
# чтобы вычислить оценку за год, ему нужно высчитать среднее арифметическое всех
# четных оценок ученика и округлить это число до ближайшего целого, не превышающее
# его. Ваша задача написать программу, которая подсчитывает годовую оценку ученика.

def calculate_even_grade(grades):
    even_grades = [grade for grade in grades if grade % 2 == 0]
    average = sum(even_grades) / len(even_grades)
    final_grade = round(average)

    return final_grade



n = int(input())
grades = list(map(int, input().split()))

result = calculate_even_grade(grades)
print(result)
