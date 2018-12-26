import datetime
import json
import urllib.request
import math


def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def url_builder(city_id):
    user_api = 'xxxxxxxxxxxxxxxxxxxxxxxx' 
    unit = 'metric' 
    api = 'http://api.openweathermap.org/data/2.5/weather?id=' 

    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        dt=time_converter(raw_api_dict.get('dt')),
    )
    return data


def data_output(data):
   
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    c=format(data['temp_max'])
    print('')
    
    print('Last update from the server: {}'.format(data['dt']))
    print('')
    return c


if __name__ == '__main__':
    try:
        a=data_output(data_organizer(data_fetch(url_builder(2643743))))
        b=data_output(data_organizer(data_fetch(url_builder(1264527))))
        d=int(a)-int(b)
        print('Current Temperature difference between Chennai,TN and London,GB is: '+str(math.fabs(d)))
    except IOError:
        print('no internet')
