from django.conf.urls import url
from django.urls import path

from .views import *


urlpatterns = [
    path('', rpt, name='rpt'),
    path('exe', exe, name='exe'),
]