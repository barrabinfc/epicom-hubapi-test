from django.test import TestCase
from .models import Category, Attribute, SKU

SKU_NAME_DEFAULT = u'Características'
CATEGORY_DEFAULT = 'CORES'
ATTR_DEFAULT = {
    'NAME': 'cor',
    'VALUE':'Azul'
}

# Create your tests here.
class SkuTestCase(TestCase):
    """
        Sku CRUD Testing
    """
    def setUp(self):
        # Tree categories
        cat_color = Category.objects.create(name=CATEGORY_DEFAULT)
        cat_price = Category.objects.create(name='PRICE', )
        cat_price_discount = Category.objects.create(name='PRICE DISCOUNT')

        # Add two color attributes
        cor = cat_color.attrs.create(name=ATTR_DEFAULT['NAME'],value= ATTR_DEFAULT['VALUE'])
        cor2 = cat_color.attrs.create(name=ATTR_DEFAULT['NAME'], value='Vermelho')
  
        # Two price attribtues
        preco = cat_price.attrs.create(name='price', value='20.0')
        preco2 = cat_price_discount.attrs.create(name='price', value='18.0')

        # One sku with everything
        sku = SKU.objects.create(name=SKU_NAME_DEFAULT)
    
    def test_sku_attribute_change(self):
        """ Attr edition """
        cor = Attribute.objects.get(name=ATTR_DEFAULT['NAME'], value=ATTR_DEFAULT['VALUE'])
        cor.value = 'Amarelo'
        cor.save()
        self.assertEqual('Amarelo', cor.value)
    
    def test_sku_reverse_mapping(self):
        """ Associate a single SKU to a attrs (reverse natural order)"""
        cor = Attribute.objects.get(name=ATTR_DEFAULT['NAME'], value=ATTR_DEFAULT['VALUE'])
        sku = SKU.objects.get(name=SKU_NAME_DEFAULT)

        sku.attrs.add(cor)
        self.assertEqual( cor.sku.first().name, sku.name )

    def test_sku_category_add_attr(self):
        """ One Category for multiple attr """
        cat = Category.objects.get(name=CATEGORY_DEFAULT)
        [cor,cor2] = Attribute.objects.filter(name=ATTR_DEFAULT['NAME'])
        cat.attrs.add(cor, cor2)
        cat.save()
        self.assertEqual( cor.categories.first().name , cat.name )

        attrs_count = cat.count_attrs()
        self.assertEqual( str(cat), "%s: %s attributes" % (CATEGORY_DEFAULT , 2))
    
    def test_sku_rm_attr(self):
        """ Removing a single attr """
        cor2 = Attribute.objects.get(name=ATTR_DEFAULT['NAME'],value=ATTR_DEFAULT['VALUE'])
        cor2.delete()
        self.assertEqual( Attribute.objects.count(), 3)

    def test_sku_category_attr_rm(self):
        """ Remove a single attr from category """
        cat = Category.objects.get(name=CATEGORY_DEFAULT)
        [cor,cor2] = Attribute.objects.filter(name=ATTR_DEFAULT['NAME'])
        cor.categories.add(cat)

        cat.attrs.remove(cor2)
        self.assertEqual( cat.count_attrs(), 1)
    
    def test_sku(self):
        """ Associate many attrs to a single SKU """
        # 3 Categories
        cat_color = Category.objects.get(name=CATEGORY_DEFAULT)
        cat_price = Category.objects.get(name='PRICE')
        cat_price_discount = Category.objects.get(name='PRICE DISCOUNT')

        # Get attributes previously categorized
        color_attrs =  Attribute.objects.filter(name=ATTR_DEFAULT['NAME'], categories__name=CATEGORY_DEFAULT)
        precos_attrs = Attribute.objects.filter(name='price', categories__name='PRICE')
        precos2_attrs = Attribute.objects.filter(name='price', categories__name='PRICE DISCOUNT')

        # Add attrs to sku
        sku = SKU.objects.get(name=SKU_NAME_DEFAULT)
        sku.attrs.add( *(list(precos_attrs) +
                         list(precos2_attrs) + 
                         list(color_attrs)))

        self.assertEqual( sku.attrs.count(), 4)