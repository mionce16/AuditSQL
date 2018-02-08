# -*- coding:utf-8 -*-
# edit by fuzongfei

from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import LoginView, LogoutView, UserProfileView, ChangePasswordView, ChangePicView

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='p_login'),
    path(r'logout/', login_required(LogoutView.as_view()), name='p_logout'),
    path(r'profile/', login_required(UserProfileView.as_view()), name='p_user_profile'),
    path(r'change_password/', login_required(ChangePasswordView.as_view()), name='p_change_password'),
    path(r'change_pic/', login_required(ChangePicView.as_view()), name='p_change_pic'),
]
