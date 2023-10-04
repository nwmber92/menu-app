from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('first_lvl/', first_lvl, name='first_lvl'),
    path('first_lvl/second_lvl/', second_lvl, name='second_lvl'),
    path('first_lvl/second_lvl/third_lvl/', third_lvl, name='third_lvl'),
]
