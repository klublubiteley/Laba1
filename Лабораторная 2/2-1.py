money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


def months_until_debt(total_money_capital, monthly_salary, monthly_spending, price_increase_rate):
    months = 0  # Количество месяцев, которые можно прожить
    current_money = total_money_capital  # Текущие деньги в бюджете

    # Проверка, хватит ли начальных средств
    if total_money_capital <= 0:
        return 0  # Невозможно прожить ни одного месяца, если денег нет

    while current_money >= 0:
        # Обновляем бюджет за счет зарплаты
        current_money += monthly_salary

        # Проверяем, хватит ли бюджета на текущие расходы
        if current_money < monthly_spending:
            break

        # Вычитаем текущие расходы
        current_money -= monthly_spending
        months += 1

        # Увеличиваем расходы на следующий месяц
        monthly_spending *= 1 + price_increase_rate

    return months


res = months_until_debt(money_capital, salary, spend, increase)
print(f'Количество месяцев, которое можно протянуть без долгов: {res}')
