"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from users.views import user_profile, user_list,profile_id
from users.forms import UserDeleteView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/<str:username>/', profile_id, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_profile, name='user_profile'),
    path('change-password/', PasswordChangeView.as_view(template_name='users/change_password.html'),
         name='change_password'),
    path('change-password/done/', PasswordChangeDoneView.as_view(template_name='users/change_password_done.html'),
         name='password_change_done'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('',include('blog.urls')),
]

