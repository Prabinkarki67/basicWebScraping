import requests
print("---Weather forecast project---")
city_name=input("Enter city name: ")
API_KEY='9553f7009aaa418885c4461496607fe2'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

response =requests.get(url)
if response.status_code==200:
    data=response.json()
    print('The weather today is: ', data['weather'][0]['description'])
    print('The temperature is: ',data['main']['temp'])
    print('The max temperature will be: ',data['main']['temp_max'])
    print('The visibility is: ',data['visibility'])
    print('The humidity is: ',data['main']['humidity'])