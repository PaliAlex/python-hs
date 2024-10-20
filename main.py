# hours = int(input("Enter Hours: "))
#
# if hours >= 12:
#     print(f'{hours}PM')
# else: print(f'{hours}AM')
from unittest import case

# hours = int(input("Enter number: "))
#
# match hours:
#     case 1:
#         print('Starting game')
#     case 2:
#         print('Ending game')
#     case _:
#         print('Invalid input')

# i = int(input("Enter Hours: "))
#
# while True:
#     if i == 2:
#         i += 1
#         print('Continue...')
#         continue
#
#     if i > 5:
#         print('Breaking...')
#         break
#
#     print(f'number:{i}')
#     i += 1

df = range(5, 11)
for i in df:
    print(i)