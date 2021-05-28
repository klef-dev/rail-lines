from django.urls import path

from .views import lines_view, stations_view

urlpatterns = [
    path('lines/', lines_view),
    path('stations/', stations_view),
]
