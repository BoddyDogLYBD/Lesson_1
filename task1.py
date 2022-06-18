"""1) Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

time = input("Введите время в секундах: ")
if int(time) == 0 or int(time) < 0 or int(time) > 43200:
    print("Вы ввели не верное значение")
elif int(time) > 0:
    hours = int(time)//3600
    minutes = (int(time)-(hours*3600))//60
    seconds = (int(time)-(hours*3600)-(minutes*60))
    print(f'Точное время: {hours}:{minutes}:{seconds}')
