zodiac_signs = {
    (1, 20): "Козерог",
    (2, 18): "Водолей",
    (3, 20): "Рыбы",
    (4, 19): "Овен",
    (5, 20): "Телец",
    (6, 20): "Близнецы",
    (7, 22): "Рак",
    (8, 22): "Лев",
    (9, 22): "Дева",
    (10, 22): "Весы",
    (11, 21): "Скорпион",
    (12, 21): "Стрелец",
}
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    day = input("Введите день рождения (1-31): ")
    month = input("Введите месяц рождения (1-12): ")

    if not day.isdigit() or not month.isdigit():
        print("Ошибка: Пожалуйста, введите числовые значения для дня и месяца.")
        continue

    day = int(day)
    month = int(month)

    if month < 1 or month > 12:
        print("Ошибка: Месяц должен быть от 1 до 12.")
        continue

    if day < 1 or day > days_in_month[month]:
        print(f"Ошибка: В этом месяце только {days_in_month[month]} дней.")
        continue

    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        sign = "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        sign = "Рыбы"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        sign = "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        sign = "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        sign = "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        sign = "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        sign = "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        sign = "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        sign = "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        sign = "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        sign = "Стрелец"
    else:
        sign = "Козерог"

    print(f"Ваш знак зодиака: {sign}")
    break
