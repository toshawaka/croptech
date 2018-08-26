from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('say_hello_world/', views.say_hello_world, name='say_hello_world')
]
