
from rest_framework import serializers
from epicom.sku.models import Attribute, Category, SKU

class SimpleAttrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id','name','value')

class SimpleCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id','url','name')

class SimpleSKUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SKU
        fields = ('url','id','name')

class AttributeSerializer(serializers.HyperlinkedModelSerializer):
    categories = SimpleCategorySerializer(many=True, required=False)
    class Meta:
        model = Attribute
        fields = ('id','name','value','categories')
        depth = 1

class CategorySerializer(serializers.HyperlinkedModelSerializer ):
    attrs = SimpleAttrSerializer(many=True)
    class Meta:
        model = Category
        fields = ('id','url','name','attrs')
        depth = 1

class SKUSerializer(serializers.ModelSerializer):
    attrs = AttributeSerializer(many=True,required=False)
    class Meta:
        model = SKU
        fields = ('id','name', 'created_at','modified_at', 'attrs')
        depth = 1

