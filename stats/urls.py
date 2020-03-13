from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stats-home'),
    path('about/', views.about, name='stats-about'),
    path('newgame/', views.newgame, name='stats-newgame')
]