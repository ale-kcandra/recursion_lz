def sklad_big_numbers(s1, s2, perenos = 0):  # рекурсивная функция сложения строк
    if not s1 and not s2 and perenos == 0:  # если строки пусты, то нечего и переносить
        return ""  # возвращаем пустую строку
    digit1 = int(s1[-1]) if s1 else 0  # берем последнюю цифру первой строки или 0
    digit2 = int(s2[-1]) if s2 else 0  # берем последнюю цифру второй строки или 0
    total = digit1 + digit2 + perenos  # складываем цифры и перенос
    current_digit = total % 10  # оставляем последнюю цифру
    new_perenos = total // 10  # вычисляем новый перенос
    return sklad_big_numbers(s1[:-1], s2[:-1], new_perenos) + str(current_digit)  # рекурсивно вызываем функцию 

num1 = input("введите первое большое число: ")  # вводим первое число
num2 = input("введите второе большое число: ")  # вводим второе число
result = sklad_big_numbers(num1, num2)  # вызываем функцию и сохраняем результат
print(f"результат: {result}")  # выводим результат