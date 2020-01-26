from django.conf.urls import url
from . import api

from .views import CustomObtainAuthToken

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
]