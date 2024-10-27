money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


def months_until_debt(money_capital, salary, spend, increase):
    months = 0  # Количество месяцев, которые можно прожить
    current_money = money_capital  # Текущие деньги в бюджете

    while current_money >= 0:
        # Обновляем бюджет за счет зарплаты
        current_money += salary

        # Проверяем, хватит ли бюджета на текущие расходы
        if current_money < spend:
            break

        # Вычитаем текущие расходы
        current_money -= spend
        months += 1

        # Увеличиваем расходы на следующий месяц
        spend *= (1 + increase)

    return months

res = months_until_debt(money_capital, salary, spend, increase)
print(f'Количество месяцев, которое можно протянуть без долгов: {res}')