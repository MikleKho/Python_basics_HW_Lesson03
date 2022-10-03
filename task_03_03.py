""" 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Без использования встроенной функции преобразования, без строк. """

def make_decimal_to_binary(decimal):
    element_position = 1
    result = 0
    while decimal > 0:
        result = result + (decimal % 2) * element_position
        element_position *= 10
        decimal //= 2
    return result

decimal = int(input("Введите число для преобразования ---> "))
print(f"Число в двоичной системе ---> {make_decimal_to_binary(decimal)}")
