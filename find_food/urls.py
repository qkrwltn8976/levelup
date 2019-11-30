from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'find_food'

urlpatterns = [
	path('', views.home, name="home"),
	path('map', views.map, name="map"),
    path('select_loc/<int:loc_id>', views.select_loc, name="select_loc"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)