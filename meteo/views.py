from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    lisbon_weather_url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'

    weather_types_response = requests.get(weather_types_url)
    weather_types_data = weather_types_response.json() if weather_types_response.status_code == 200 else {}

    weather_types = {item['idWeatherType']: item['descWeatherTypePT'] for item in weather_types_data['data']}

    lisbon_weather_response = requests.get(lisbon_weather_url)
    lisbon_weather_data = lisbon_weather_response.json() if lisbon_weather_response.status_code == 200 else {}

    today_weather = lisbon_weather_data['data'][0] if 'data' in lisbon_weather_data else {}

    context = {
        'city': 'Lisboa',
        'date': today_weather.get('forecastDate', ''),
        'min_temp': today_weather.get('tMin', ''),
        'max_temp': today_weather.get('tMax', ''),
        'weather_description': weather_types.get(today_weather.get('idWeatherType', ''), ''),
        'weather_type_id': today_weather.get('idWeatherType', '')
    }
    return render(request, 'meteo/index.html', context)

def previsao(request):
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cities_response = requests.get(cities_url)
    cities_data = cities_response.json() if cities_response.status_code == 200 else {}

    cities = cities_data['data'] if 'data' in cities_data else []

    context = {
        'cities': cities,
    }
    return render(request, 'meteo/previsao.html', context)

def previsao_5_dias(request):
    city_id = request.GET.get('city_id', '1110600')  # ID padrão de Lisboa
    weather_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    weather_response = requests.get(weather_url)
    weather_data = weather_response.json() if weather_response.status_code == 200 else {}

    weather_types_response = requests.get(weather_types_url)
    weather_types_data = weather_types_response.json() if weather_types_response.status_code == 200 else {}

    weather_types = {item['idWeatherType']: item['descWeatherTypePT'] for item in weather_types_data['data']}

    forecasts = weather_data['data'][:5] if 'data' in weather_data else []

    for forecast in forecasts:
        forecast['weather_description'] = weather_types.get(forecast.get('idWeatherType', ''), '')

    context = {
        'forecasts': forecasts,
        'city': city_id,
    }
    return render(request, 'meteo/previsao_5_dias.html', context)

# Views para a API
def lista_cidades(request):
    url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(url)
    data = response.json()['data']
    cidades = [{'id': item['globalIdLocal'], 'nome': item['local']} for item in data]
    return JsonResponse(cidades, safe=False)

def previsao_hoje(request, cidade_id):
    url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
    response = requests.get(url)
    data = response.json()['data'][0]
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    weather_types_response = requests.get(weather_types_url)
    weather_types_data = weather_types_response.json()
    weather_types = {item['idWeatherType']: item['descWeatherTypePT'] for item in weather_types_data['data']}
    data['weather_description'] = weather_types[data['idWeatherType']]
    data['icon'] = f'/static/meteo/icons/w_ic_d_{str(data["idWeatherType"]).zfill(2)}anim.svg'
    return JsonResponse(data)

def previsao_cinco_dias(request, cidade_id):
    url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
    response = requests.get(url)
    data = response.json()['data'][:5]
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    weather_types_response = requests.get(weather_types_url)
    weather_types_data = weather_types_response.json()
    weather_types = {item['idWeatherType']: item['descWeatherTypePT'] for item in weather_types_data['data']}
    for forecast in data:
        forecast['weather_description'] = weather_types[forecast['idWeatherType']]
        forecast['icon'] = f'/static/meteo/icons/w_ic_d_{str(forecast["idWeatherType"]).zfill(2)}anim.svg'
    return JsonResponse(data, safe=False)

def api_documentation(request):
    return render(request, 'meteo/api_documentation.html')
