import random
import time

name = input('Имя введи:')

print(f'Очень приятно, {name}', 'я предлагаю тебе угадать число, (1 до 10)')

user_number = input('Введи число,' + name + ':')

random_number = random.randint(1, 1)

if  user_number == random_number:
    print( name + ", ты угадал, что удивительно." )

else:
    print( name + ", ты естесственно не угадал.")
    print(f'Число было {random_number}, тупень')
    input('Дальше (Enter)')

mnenie = input('Ваше мнение?))')
print('ДА НИКОГО НЕ ЕБЕТ ТВОЕ МНЕНИЕ! ТВОЯ ВИНДА У МЕНЯ, СЛАДКИЙ')

while True:
    print("Завершение программы...")
    time.sleep(60) # Delay for 1 minute (60 seconds).
