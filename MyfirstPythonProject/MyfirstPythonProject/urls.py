"""MyfirstPythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import  url, include
from django.contrib import admin
from django.urls import path
from testapp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home/', views.home_page_view),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^welcome/', views.welcome_view),
    url(r'^logout/', views.logout_view),
    url(r'^signup/', views.signup_view),
    url(r'^dashboard/', views.retrieve_view),
    url(r'^membership/', views.create_view),
    url(r'^confirmation/', views.create_view),
    url(r'^delete/(?P<id>\d+)/$', views.delete_view),
    url(r'^cancellation/', views.delete_view),
    url(r'^update/(?P<id>\d+)/$', views.update_view),
    url(r'^updated/', views.update_view),

]


