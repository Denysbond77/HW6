seconds = int(input("Введіть кількість секунд (від 0 до 8640000): "))

if seconds < 0 or seconds > 8640000:
    print("Число повинно бути від 0 до 8640000.")

else:
    days, rem = divmod(seconds, 24 * 60 * 60)
    hours, rem = divmod(rem, 60 * 60)
    min, seconds = divmod(rem, 60)

    last_digit = days % 10
    last_two_digits = days % 100

    if 11 <= last_two_digits <= 19:
        day1 = "днів"
    elif last_digit == 1:
        day1 = "день"
    elif 2 <= last_digit <= 4:
        day1 = "дні"
    else:
        day1 = "днів"

    ftime = f"{str(hours).zfill(2)}:{str(min).zfill(2)}:{str(seconds).zfill(2)}"
    print(f"{days} {day1}, {ftime}")


