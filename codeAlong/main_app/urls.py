from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('practice/', views.practice, name='practice'),
    path('study/', views.study, name="study"),
    path('login/', views.login, name="login"),
]