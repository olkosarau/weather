from django.urls import path
from weather.views import index


urlpatterns = [
    path('weather/', index),

]
