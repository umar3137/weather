# https://openweathermap.org/
# a86fe122e79d9736005d012e9c4ff44d


# https://api.openweathermap.org/data/2.5/weather?q=Воронеж&appid=a86fe122e79d9736005d012e9c4ff44d&units=metric


import requests


def get_weather(city, api_key):
#   print(f"Вы ввели {city}. Ваш ключ api:{api_key}")
  url="https://api.openweathermap.org/data/2.5/weather?" 
  complete_url = f"{url}q={city}&appid={api_key}&units=metric"
  print(complete_url)

  r =  requests.get(complete_url)
  print(r)
  print('Hello,')
  data = r.json()
  print(type(data))

  temp = data["main"]["temp"]
  print(f"Температура: {temp}")

  weather = data["weather"][0]['description']
  print(f"Погода: {weather}")

  pressure = data["main"]["pressure"]
  print(f'Давление: {pressure}')
  

  humidity = data['main']['humidity']
  print(f'Влажность: {humidity}')

  speed = data['wind']['speed']
  print(f'Скорость ветра: {speed}')




def main():
  print("Узнай погоду: ")

  city = input("Введите свой город: ")
  api_key = "a86fe122e79d9736005d012e9c4ff44d"

  get_weather(city,api_key)


main()















