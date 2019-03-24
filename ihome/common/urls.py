from django.urls import path

from common.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('checked_index/', checked_index, name='checked_index'),
]
