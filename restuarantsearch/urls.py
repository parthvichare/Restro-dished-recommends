from django.urls import path
from . import views
# from . import api_views

urlspattern=[
    path('search/', views.search,name='search')
]