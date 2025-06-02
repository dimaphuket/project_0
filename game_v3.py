"""Игра угадай число
Компьютер сам загадывает и сам угадывает число по оптимальному алгоритму
"""

import numpy as np


def median_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number=50  # предполагаемое число (пытаемся взять среднее значение)
    minimum = 1  # нижняя граница поиска
    maximum = 100  # верхняя граница поиска
    final_step = False  # флаг того, что следующий шаг будет последним
    last_predict_number = 0  # последнее предсказанное число
    while True:
        count += 1 # увеличиваем счетчик попыток
        if number == predict_number:
            break  # выход из цикла если угадали
        else:
            # обновляем границы поиска
            if predict_number > number:
                maximum = predict_number
            elif predict_number < number:
                minimum = predict_number
            last_predict_number = predict_number  # сохраняем последнее предсказанное число
            # если мы дошли до того, что диапазон поиска сужен до 1, то дальше идём на 
            # шаг вперед
            if final_step:
                predict_number = last_predict_number +1
            # если мы ещё в поиске - берём медиану между минимумом и максимумом (округляя вниз)
            else:
                predict_number = int(np.median([minimum,maximum]))
            # если между предсказанным и последним предсказанным разница в 1 то переходим
            # к винальному шагу
            if (predict_number - last_predict_number)==int(1):
                final_step = True
    return count


def score_game(median_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    for number in random_array:
        count_ls.append(median_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(median_predict)
