"""
URL configuration for HelloWorld project.

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
from django.urls import path
from django.urls import re_path
from django.urls import include
from django.contrib import admin



from login import views
urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('index/', views.index),
    path("login-post/", views.login_post),
    path("register-post/", views.register_post),
    path("addProject-post/", views.addProject_post),
    path("listProject/", views.list_project),
    path("searchProject/", views.search_post),
    path("deleteProjectByNameList/", views.delete_post),
    path("reviseProjectByName/", views.revise_project),
    path("reviseProject-post/", views.revise_project_post),
    path('admin/', admin.site.urls),
]