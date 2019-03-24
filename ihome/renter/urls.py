from django.urls import path

from renter.views import *

urlpatterns = [
    path('orders/', orders, name='orders'),
    path('search/', search, name='search'),
    path('detail/<int:id>', detail, name='detail'),
    path('booking/<int:id>', booking, name='booking'),
]