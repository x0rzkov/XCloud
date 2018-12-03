from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('welcome', views.welcome, name='welcome'),
    url('fbp', views.fbp, name='fbp'),
    url('detectface', views.detect_face, name='detectface'),
]
