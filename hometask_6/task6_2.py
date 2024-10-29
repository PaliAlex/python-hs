SECONDS_IN_A_DAY = 86400
SECONDS_IN_A_HOUR = 3600
SECONDS_IN_A_MINUTE = 60
days_word = ''

inputNumber = int(input('Введіть кількість секунд : '))

days = divmod(inputNumber, SECONDS_IN_A_DAY)
hours = divmod(days[1], SECONDS_IN_A_HOUR)
minutes = divmod(hours[1], SECONDS_IN_A_MINUTE)

hours_amount = str(hours[0]).zfill(2)
minutes_amount = str(minutes[0]).zfill(2)
seconds_amount = str(minutes[1]).zfill(2)

if days[0] % 100 in [11, 12, 13, 14]:
    days_word = 'днів'
elif days[0] % 10 == 1:
    days_word = 'день'
elif days[0] % 10 in [2, 3, 4]:
    days_word = 'дні'
else:
    days_word = 'днів'

print(f'{days[0]} {days_word}, {hours_amount}:{minutes_amount}:{seconds_amount}')


# Якщо останні дві цифри числа — 11, 12, 13 або 14, завжди використовуємо "днів".
# Якщо остання цифра — 1 (але не 11), використовуємо "день".
# Якщо остання цифра — 2, 3 або 4 (але не 12, 13, 14), використовуємо "дні".
# В усіх інших випадках — "днів".