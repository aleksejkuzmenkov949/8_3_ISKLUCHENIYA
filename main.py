def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    try:
        for number in numbers:
            if isinstance(number, int) or isinstance(number, float):
                result += number
            else:
                incorrect_data += 1
    except TypeError as e:
        print('Некорректный тип данных для подсчёта суммы -', e)
        return None, None

    return result, incorrect_data


def calculate_average(numbers):
    try:
        sum_result, incorrect_data = personal_sum(numbers)
        if sum_result == 0:
            raise ZeroDivisionError
        average = sum_result / len(numbers)
    except ZeroDivisionError as e:
        print('Деление на 0')
        return 0
    except TypeError as e:
        print('В numbers записан некорректный тип данных')
        return None

    return average


# Вызов функции calculate_average с разными данными
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
