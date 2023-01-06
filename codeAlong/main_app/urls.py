from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('practice/', views.practice, name='practice'),
    path('practice/<int:leetcode_id>/', views.practice_details, name='detail'),
    path('study/', views.study, name="study"),
    # path('login/', views.login, name="login"),
    # Django's built-in auth doesn't provide a URL || view for singing up...Gotta make my own.
    path('accounts/signup/', views.signup, name='signup'),
]