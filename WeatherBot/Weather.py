import python_weather
import asyncio

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL,locale="ru-RU")

    # fetch a weather forecast from a city
    weather = await client.find("Moscow")

    celsius = (weather.current.temperature - 32) * 5/9

    print(str(round(celsius)) + " градусов")

    print(weather.current.sky_text)

    print(weather.location_name)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
