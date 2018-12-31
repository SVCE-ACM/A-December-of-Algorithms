import requests, json 
api_key = "62ndkcdjkhv948kcpamc10294mgog" #duplicate key
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name1 = input("Enter the first city name : ")
city_name2 = input("Enter the second city name : ") 
complete_url1 = base_url + "appid=" + api_key + "&q=" + city_name1 
response1 = requests.get(complete_url1) 
x1 = response1.json() 
if x1["cod"] != "404": 
    y1 = x1["main"]  
    temp1=y1["temp"] 
else: 
    print(" City 1 Not Found ")
complete_url2 = base_url + "appid=" + api_key + "&q=" + city_name2 
response2 = requests.get(complete_url2) 
x2 = response2.json() 
if x2["cod"] != "404": 
    y2 = x2["main"]  
    temp2=y2["temp"] 
else: 
    print(" City 2 Not Found ")
diff=temp1-temp2
print('Current Temperature difference between',city_name1,'and',city_name2,'is',abs(diff),'degree celsius')
