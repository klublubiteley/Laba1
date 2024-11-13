import json


def task() -> float:
    # Путь к JSON файлу
    file_path = 'input.json'

    # Читаем JSON файл
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Инициализируем сумму
    total_sum = 0.0

    # Проходим по всем элементам в данных
    for item in data:
        # Проверяем, что ключи существуют
        if 'score' in item and 'weight' in item:
            # Вычисляем произведение и добавляем к общей сумме
            total_sum += item['score'] * item['weight']

    # Возвращаем округленное значение
    return round(total_sum, 3)


# Выводим результат
print(task())
