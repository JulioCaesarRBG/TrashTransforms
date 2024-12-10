from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_sensor_data, name='get_data'),
]

