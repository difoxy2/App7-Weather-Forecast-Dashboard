import requests

#get api key stored in txt
with open('APIkey.txt','r') as f:
    apikey=f.read()

# def get_data(days,city):

#     #get lat and lon of city
#     url1=f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={apikey}'
#     respond1 = requests.get(url1).json()[0]
#     lat = respond1['lat']
#     lon = respond1['lon']
    
#     #get weather data
#     url2=f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric&cnt={int(days)*8}'
#     respond2 = requests.get(url2).json()['list']
#     date_time_array = [i['dt_txt'] for i in respond2]
#     tempreture_array = [i['main']['temp'] for i in respond2]

#     return date_time_array, tempreture_array



def get_data(days,city):
    url1=f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric'
    respond1 = requests.get(url1).json()['list']
    respond1_reduced_by_days = respond1[:int(days)*8] # data is per 3 hours --> 1 day has 8 data points

    date_time_array = [i['dt_txt'] for i in respond1_reduced_by_days]
    tempeture_array = [i['main']['temp'] for i in respond1_reduced_by_days]
    sky_array = [i['weather'][0]['main'] for i in respond1_reduced_by_days]
    
    return date_time_array, tempeture_array, sky_array


if __name__=="__main__":
    print(get_data(3,'London'))