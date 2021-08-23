import pprint

import requests
from django.shortcuts import render
from .models import City
from .form import CityForm


def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=631c936aae60c0952f107243d58bcfcf"
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    cities = City.objects.all()
    all_city = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        all_city.append(city_info)

    res_info = {'all_info': all_city, 'form': form}
    return render(request, 'weather/index.html', res_info)
