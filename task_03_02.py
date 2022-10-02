""" 2. Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
in
4
out
[2, 5, 8, 10]
[20, 40]
in
5
out
[2, 2, 4, 8, 8]
[16, 16, 4] """

from random import sample


def make_list(number_elem):
    list = sample(range(1, number_elem * 2), number_elem)
    return list


def calc_multiplicate(list):
    result = []
    for i in range(int(len(list) / 2)):
        result.append(list[i] * list[len(list) - 1 - i])
    if (len(list) % 2 == 1):
        result.append(list[int(len(list) / 2)])

    return result


number_elem = int(input("Введите количество чисел ---> "))
list = make_list(number_elem)
print(f"Список чисел ---> {list}")
print(f"Список произведений ---> {calc_multiplicate(list)}")
