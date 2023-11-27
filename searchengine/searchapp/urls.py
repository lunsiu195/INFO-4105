# searchapp/urls.py
from django.urls import path
from .views import search_view, home, image_search

app_name = 'searchapp'

urlpatterns = [
    path('search/', search_view, name='search'),
    path('', home, name='home'),
    path('searchapp/', image_search, name='image_search')
]
