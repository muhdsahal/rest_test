"""
URL configuration for restapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import IsAuthenticated
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.register.as_view(),name='register'),
    path('login/',obtain_auth_token,name="login"),
    path('welcome',views.welcome.as_view(),name='welcome'),
    path('userDetails/<int:pk>/',views.userDetails.as_view(),name="userDetails"),
    path('paginationApi',views.paginationApi.as_view(),name='paginationApi')

]
