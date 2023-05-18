from django.urls import path
from .views import *


urlpatterns = [
    path('', template1_index, name='template1_index'),
]