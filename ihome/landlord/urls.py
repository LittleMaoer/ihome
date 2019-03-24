from django.urls import path

from landlord.views import *

urlpatterns = [
    path('auth/', auth, name='auth'),
    path('lorders/', lorders, name='lorders'),
    path('my/', my, name='my'),
    path('myhouse/', myhouse, name='myhouse'),
    path('newhouse/', newhouse, name='newhouse'),
    path('profile/', profile, name='profile'),
]