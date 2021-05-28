from django.urls import path

from .views import lines_view, stations_view, home_view

urlpatterns = [
    path('', home_view),
    path('api/lines/', lines_view),
    path('api/stations/', stations_view),
]
