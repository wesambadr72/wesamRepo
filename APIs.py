import requests

# baseUrl = "https://pokeapi.co/api/v2"

# def get_pokemonInfo(name):
#     url=f"{baseUrl}/pokemon/{name}"
#     response = requests.get(url)
#     if response.status_code==200:
#         pokemonData=response.json()
#         return pokemonData
#     else:
#         print(f"error {response.status_code}")

# dict={'name':"pokemon",'age':34}
# print(dict.get('age'))
# print(dict)

# pokemonName="ditto"
# pokeInfo=get_pokemonInfo(pokemonName)

# if pokeInfo:
#     print(f"Name: {pokeInfo['name'].capitalize()}")
#     print(f"ID: {pokeInfo['id']}")
#     print(f"Height: {pokeInfo['height']}")
#     print(f"Weight: {pokeInfo['weight']}")
 

# def greeting():
#     print('Hi!')
#     yield 1
#     print('How are you?')
#     yield 2
#     print('Are you there?')
#     yield 3

# massage =greeting()
# print(next(massage))
# print(next(massage))
# print(next(massage))

# ages=[5,12,17,18,24,32]

# fucl = [age + 2 if age >= 18 else 0 for age in ages]
# print(list(filter((lambda age:age>=18),ages))) #[18,24,32]
# print(fucl)
# print(max(min(min(max(max(1,2),5),4),8),7))

# APIkey="64dacce567956b09d26346fc440cc7e1"

# def get_weatherInfo(cityName):
#     url=f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&units=metric&appid={APIkey}"
#     response=requests.get(url)
#     if response.status_code==200:
#         weatherData=response.json()
#         return weatherData
#     else:
#         print(f"error {response.status_code}")

# def DescribeTheHumidity(humidity):
#     if 0<=humidity <=30:
#         return "Dry air"
#     elif 31<=humidity <=60:
#         return "Moderate humidity"
#     elif 61<=humidity <=100:
#         return "High humidity"
    

# city=input("Enter a city name: ")
# weatherOfCity = get_weatherInfo(city)

# if weatherOfCity:
#     print(f"City: {weatherOfCity['name']}") #City name
#     print(f"Country: {weatherOfCity['sys']['country']}")# Country
#     print(f"Weather: {weatherOfCity['weather'][0]['main']}")#Weather
#     print(f"Description: {weatherOfCity['weather'][0]['description']}")#Description of the weather
#     print(f"Temperature: {weatherOfCity['main']['temp']}°C")# Temperature in Celsius
#     print(f"Real feels: {weatherOfCity['main']['feels_like']}°C") # Real feels in Celsius
#     Humidity=weatherOfCity['main']['humidity']
#     print(f"Humidity: {Humidity}%") # Humidity
#     print(DescribeTheHumidity(Humidity))
#     print(f"Wind speed:{weatherOfCity['wind']['speed']} km/h") #Wind speed in km/h


apiurl='https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=~Naruto'
apiurl2='https://kitsu.io/api/edge/anime?filter[text]=naruto'
response=requests.get(apiurl2)

if response.status_code==200:
    # print(response.json())
    data = response.json()
    print(data['data'][0]['attributes']['titles']['en_jp'])
    print(data['data'][0]['attributes']['slug'])
