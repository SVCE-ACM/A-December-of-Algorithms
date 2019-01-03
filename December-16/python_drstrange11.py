# Dec 16
import requests
import datetime


def get_temp(URL, city):
    params = dict(
        q=city,
        appid="eb971f61d87786bc291ac670844dd996"  # Dummy id
    )
    res = requests.get(url, params=params, headers={
                       "Accept": "application/json"})
    data = res.json()
    return data['main']['temp']


url = "http://api.openweathermap.org/data/2.5/weather"
city_1 = 'London,GB'
city_2 = 'Chennai,IN'
d = datetime.datetime.now()
k = d.strftime("%H:%I %p %x")
print(f"Taken at {k}")

print(
    f"Current difference between {city_1} and {city_2} is {round(abs(get_temp(url,city_1)-get_temp(url,city_2)),2)} \xb0C")

# Sample I/O
# Taken at 10:10 AM 01/03/19
# Current difference between London,GB and Chennai,IN is 22.75 °C
