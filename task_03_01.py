""" 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
in
5
out
[10, 2, 3, 8, 9]
22 """

from random import sample

def make_list(number_elem):
    list = sample(range(1, number_elem * 2), number_elem)
    return list


def calc_sum(list):
    result = 0
    for i in range(0, len(list), 2):
        result = result + list[i]
    return result


number_elem = int(input("Введите количество чисел ---> "))
list = make_list(number_elem)
print(f"Список чисел ---> {list}")
print(f"Сумма нечетных элементов ---> {calc_sum(list)}")

