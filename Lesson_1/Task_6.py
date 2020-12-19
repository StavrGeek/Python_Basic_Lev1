first_day_res = int(input("Введите результат пробежки за первый день в км: "))
wish_res = int(input("Введите желаемый результат в км: "))
result_day = 1
result = first_day_res

while result <= wish_res:
    result += result * 0.1
    result_day += 1
print(f"На {result_day:d}-й день спортсмен достиг результата не менее {wish_res} километров")
