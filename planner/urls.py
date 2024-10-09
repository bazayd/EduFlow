# planner/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import signup_view

urlpatterns = [
    path('', views.index, name='index'),  # Route for the homepage
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
]