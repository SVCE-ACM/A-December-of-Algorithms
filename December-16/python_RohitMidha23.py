import pyowm 

# Creating owm with my API Key
owm = pyowm.OWM('my-api-key-here')

city1 = input("Enter city 1: ")
city2 = input("Enter city 2: ")

w1 = owm.weather_at_place(city1)
w2 = owm.weather_at_place(city2)

weather_difference = w1.get_temperature('celsius')-w2.get_temperature('celsius')

print(weather_difference)