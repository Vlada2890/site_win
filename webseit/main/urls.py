from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('types', views.types),
    path('grown', views.grown),
    path('food', views.food),
]
