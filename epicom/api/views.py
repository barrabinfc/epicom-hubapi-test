from rest_framework import viewsets

from django.contrib.auth.models import User, Group
from epicom.sku.models import Attribute, Category, SKU

from epicom.api.serializers import UserSerializer, GroupSerializer
from epicom.sku.serializers import AttributeSerializer, CategorySerializer, SKUSerializer

"""
    Users/Groups
"""
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

"""
    SKU, SKUCategory, SKUAttribute
"""
class AttrViewSet(viewsets.ModelViewSet):
    """ Attribute endpoint to edit attributes of SKU """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """ Category Attr endpoint that allows to edit category """
    queryset = Category.objects.all()
    serializer_class = AttributeSerializer

class SKUViewSet(viewsets.ModelViewSet):
    """ SKU view and edit endpoint """
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer