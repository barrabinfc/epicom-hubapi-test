"""composeexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  path(r'^blog/', include(blog_urls))
"""
from django.urls import path, include
from django.contrib import admin

from epicom.sku.urls import urlpatterns as sku_urls
from epicom.api.urls import urlpatterns as api_urls
#from .produto.urls import urlpatterns as produto_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sku/', include(sku_urls)),
    path(r'api/', include(api_urls))
    #path('produto/', include(produto_urls))
]
