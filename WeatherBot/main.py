from aiogram import Bot, Dispatcher, executor, types

import python_weather



# bot init

bot = Bot(token="5483518862:AAGo-Tclr-RC493OyX91EpGeP2IAfY2RNfw")
dp = Dispatcher(bot)

client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")

# echo
@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celsius = (weather.current.temperature - 32) * 5 / 9

    resp_msq = weather.location_name + "\n"
    resp_msq += f"Текущая температура: {round(celsius)} \n"
    resp_msq += f"состояние погоды: {weather.current.sky_text} \n"

    if celsius <= 10:
        resp_msq += "\n\n Еба у вас там... дубу дать можно!"
    else:
        resp_msq += "\n\n Ниче, жить можно, ДУБУ НЕ ДАШЬ!!"

        if message.text == "Нерюнгри":
            resp_msq += "\n\n Если кодер, что создал это из Нерюнгри - это не значит, что нужно вбивать ваш долбучий Нерюнгри!!"


    await message.answer(resp_msq)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
