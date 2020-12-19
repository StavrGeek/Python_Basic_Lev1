user_seconds = int(input("Пожалуйста введите количество секунд: "))
print(f"Текущее время {(user_seconds//3600)%24:02}:{(user_seconds//60)%60:02}:{user_seconds%60:02}")