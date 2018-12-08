from django.conf.urls import url, include
from rest_framework import routers

from epicom.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'sku', views.SKUViewSet )
#router.register(r'sku/attr', views.AttrViewSet)
#router.register(r'sku/category', views.CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
