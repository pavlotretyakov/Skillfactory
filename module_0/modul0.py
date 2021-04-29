import numpy as np

count: int = 0  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
           Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, 101)

    while number < predict:
        count += 1
        if number > predict:
            predict += 10
        elif predict > number:
            predict -= 10
            if number > predict:
                predict += 1
            elif number < predict:
                predict -= 10
    return(count)


count = (game_core_v2(number))

print(f"Вы угадали число {number} за {count} попыток.")