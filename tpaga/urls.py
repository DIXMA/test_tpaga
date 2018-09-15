"""tpaga URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from app.views import Accounts, AccountsUpdate

#router = routers.DefaultRouter()
#router.register(r'accounts', Accounts.as_view())

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/$', Accounts.as_view()),
    url(r'^accounts/update/(?P<pk>[0-9]+)/$', AccountsUpdate.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
