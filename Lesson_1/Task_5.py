user_profit = int(input("Введите значение выручки фирмы: "))
user_expenses = int(input("Введите значение издержек фирмы: "))

if user_profit > user_expenses:
    print(f"Ваша фирма приносит прибыль, значение рентабельности составляет: {user_profit/user_expenses}")
    staff_count = int(input("Введите количество сотрудников фирмы: "))
    print(f"Выручка на каждого сотрудника составляет: {user_profit/staff_count}")
else:
    print("Ваша фирма работает в убыток")