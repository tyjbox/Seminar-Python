import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot) #в aiogram хендлерами управляет диспетчер


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет! Напиши мне название города (на английском языке) и я пришлю сводку погоды!')

@dp.message_handler()
async def get_weather(message: types.Message):
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
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'# units=metric перевод градусов в цельсия
        )
        data = r.json()

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

        await message.reply(f'***{datetime.datetime.today().strftime("%Y-%m-%d %H:%M")}***\n' # вывод текущей даты
              f'Погода в городе: {city}\nТемпература: {cur_weather} С° {wd}\n'
              f'Влажность: {humidity} %\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\nВосход солнца: {sunrise_timestamp}\n'
              f'Закат солнца: {sunset_timestamp}\nПродолжительность дня: {lenght_of_the_day}\n'
              f'***Хорошего дня!***😉'
             )
    except:
        await message.replyprint('\U00002620 Проверьте правильное написание города!') 




if __name__== '__main__':
    executor.start_polling(dp)