user_number = int(input("Введите целое положительное число: "))
max_value = 1
while user_number > 0:
    result = user_number % 10
    if result >= max_value:
        max_value = result
        user_number //= 10
    else:
        user_number //= 10
print(max_value)
