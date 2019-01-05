
from weather import Weather, Unit

def GetCity():
	city = input("Enter the name of the city --> ")
	return city

def GetCityTemperature(city):
	weather = Weather(unit=Unit.CELSIUS)
	location = weather.lookup_by_location(city)
	forecasts = location.forecast

	return forecasts[0].high


city1 = GetCity()
city2 = GetCity()

temp1 = int(GetCityTemperature(city1))
temp2 = int(GetCityTemperature(city2))

diff = temp2 - temp1

print("\n")

print("The temperature in {a} is {b}.".format(a=city1, b=temp1))
print("The temperature in {a} is {b}.".format(a=city2, b=temp2))

if (diff) < 0 :
	diff = diff * -1

print("The temperature difference is {a}.".format(a=diff))
