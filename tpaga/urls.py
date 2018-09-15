"""
tpaga URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app.views import Accounts, AccountsUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/$', Accounts.as_view()),
    url(r'^accounts/update/(?P<pk>[0-9]+)/$', AccountsUpdate.as_view()),
]
