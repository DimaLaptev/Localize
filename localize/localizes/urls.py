from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from . import views

app_name = 'localizes'

urlpatterns = [
    path('', views.index, name='index'),
]
