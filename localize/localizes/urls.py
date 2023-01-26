from django.urls import path
from . import views

app_name = 'localizes'

urlpatterns = [
    path('', views.index, name='index'),
]
