from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'find_food'

urlpatterns = [
	path('', views.home, name="home"),
	path('map', views.map, name="map"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)