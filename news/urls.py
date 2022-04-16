from cgitb import handler
from unicodedata import name
from django import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('userguide', userguide, name='userguide'),
    path('export_excel', export_excel, name='export-excel'),
    path('news/', news, name='news'),
    path('news/<slug:new_slug>/', show_new, name='new'),
    path('tarifs/', tariffs, name='tariffs'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('director/', director, name='director'),
    path('requisites/', requisites, name='requisites'),
    path('search/', search, name='search'),
    path('consumerinfo/', consumerinfo, name='consumerinfo'),
    path('sitemap/', sitemap, name='sitemap'),
]
