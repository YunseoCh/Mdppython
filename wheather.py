#날씨 습도 온도 출력
#날씨 API
import requests
import json

city = "Seoul" #도시
apiKey = "ed3a431559f647fbbdcb6ac46e611e46" #내 apikey 
lang = 'kr' #언어
units = 'metric' #화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
result = json.loads(result.text)

print(result)

name = result['name']
lon = result['coord']['lon'] 
lat = result['coord']['lat']
weather = result['weather'][0]['main']
temperature = result['main']['temp']
humidity = result['main']['humidity']

print("도시 : ", name) 
print("경도, 위도 : ", lon, ', ', lat)
print("날씨 : ", weather)
print("온도", temperature)
print("습도", humidity)