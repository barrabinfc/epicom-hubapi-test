from epicom.sku.models import Attribute, Category, SKU
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'categories')

class SKUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SKU
        fields = ('name', 'created_at','modified_at','attrs')

class AttributeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attribute
        fields = ('name', 'value','sku')
