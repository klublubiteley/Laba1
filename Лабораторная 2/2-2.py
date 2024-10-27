salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

def calculate_safety_net(salary, spend, months, increase_rate):
    money_capital = 0  # Изначально подушка безопасности равна нулю
    total_needed_capital = 0  # Суммарная потребная подушка безопасности за 10 месяцев

    for month in range(months):
        # В первый месяц расходы не увеличиваются
        if month > 0:
            spend *= (1 + increase_rate)  # Увеличиваем расходы на заданный процент

        # Определяем нехватку средств после зарплаты
        deficit = spend - salary

        if deficit > 0:
            total_needed_capital += deficit  # Увеличиваем суммарную потребность в подушке безопасности

    # Округление до целого числа
    money_capital = round(total_needed_capital)

    return money_capital

# Рассчитываем необходимую подушку безопасности
needed_capital = calculate_safety_net(salary, spend, months, increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {needed_capital}")