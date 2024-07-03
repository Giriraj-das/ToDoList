from django.urls import path
from core import views

urlpatterns = [
    path('signup', views.UserCreateView.as_view(), name='signup'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('profile', views.UserProfileView.as_view(), name='retrieve-update-destroy-user'),
    path('update_password', views.UserPasswordUpdateView.as_view(), name='update-password'),
]
