# searchapp/urls.py
from django.urls import path
from .views import search_view, home

app_name = 'searchapp'

urlpatterns = [
    path('search/', search_view, name='search'),
    path('', home, name='home'),
]
