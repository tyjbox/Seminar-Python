import requests
import datetime
from pprint import pprint
from config import open_weather_token




def get_weather(city, open_weather_token):

    # словарь информации о сотоянии погоды c эмодзи
    code_to_smile = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain':'Дождь \U00002614',
        'Drizzle':'Дождь \U00002614',
        'Thunderstorm':'Гроза \U000026A1',
        'Snow':'Снег \U0001F328',
        'Mist':'Туман \U0001F32B'
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'# units=metric перевод градусов в цельсия
        )
        data = r.json()
        # pprint(data)# получаем полные данные о городе 

        city = data['name']# данные берем из консоли через  pprint(data)
        cur_weather = data['main']['temp'] # main - блок, temp - ключ

        weather_description = data['weather'][0]['main']
        if  weather_description in code_to_smile:
            wd = code_to_smile[ weather_description]
        else:
            wd = 'Посмотри в окно, не пойму что там за погода!'

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])# преобразуем в читаемый формат через модуль datetime
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        print(f'***{datetime.datetime.today().strftime("%Y-%m-%d %H:%M")}***\n' # вывод текущей даты
              f'Погода в городе: {city}\nТемпература: {cur_weather} С° {wd}\n'
              f'Влажность: {humidity} %\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\nВосход солнца: {sunrise_timestamp}\n'
              f'Закат солнца: {sunset_timestamp}\nПродолжительность дня: {lenght_of_the_day}\n'
              f'Хорошего дня!😉'
             )
    except Exception as ex:
        print(ex)
        #print('Проверьте название города!')



def main():
    city = input('Введите название города: ')
    get_weather(city, open_weather_token)

if __name__== '__main__':
    main()