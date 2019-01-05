import requests

def Weather() :
    url1 = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=DummyAPIKey"
    data1= requests.get(url1).json()
    t1 = float(data1["main"]["temp"])
    t1 = t1-273.15
    url2 = "http://api.openweathermap.org/data/2.5/weather?q=Chennai,IN&APPID=DummyAPIKey"
    data2= requests.get(url2).json()
    t2 = float(data2["main"]["temp"])
    t2 =  t2-273.15
    print("Temparture at London: %.2f\u2103" % round(t1,2))
    print("Temparture at Chennai: %.2f\u2103" % round(t2,2))
    print("Difference in Temperature = %.2f\u2103" % round(t2-t1,2))
        
def main():
   Weather()
    
if __name__ == "__main__":
    main()
