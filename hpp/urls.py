from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('prediction', views.prediction, name='prediction'),
    path('outcome', views.outcome, name='outcome'),
    path('about', views.about, name='about'),
]
