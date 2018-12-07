from random import randint
from django.test import TestCase
from .models import Category, Attribute, SKU

SKU_NAME_DEFAULT = u'Características'
CATEGORY_DEFAULT = 'CORES'
ATTR_DEFAULT_NAME = 'cor'

COLOR_QTD = 10
PRICE_QTD = 10

def color_format(r=randint(0,255),g=randint(0,255),b=randint(0,255)):
    """ Single color to hex-format """
    return '#%02X%02X%02X' % (r,g,b)

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

        # Add 10 color attributes
        for i in range(0,COLOR_QTD):
            cat_color.attrs.create(name=ATTR_DEFAULT_NAME, value=color_format()) 
  
        # Add 10 prices
        START_PRICE = 5
        STEP_PRICE = 5
        for price in range(START_PRICE, (START_PRICE*PRICE_QTD)+1, STEP_PRICE):
            cat_price.attrs.create(name='price', value=str(price))

        # Add a Price with category discount 
        preco_discount = cat_price_discount.attrs.create(name='price', value='18.0')

        # Sku with attrs attached
        sku = SKU.objects.create(name=SKU_NAME_DEFAULT)
        sku_inprice = SKU.objects.create(name='prices')
        sku_inprice.attrs.add( *(list(cat_price.attrs.all() )))

    
    def test_sku_attribute_change(self):
        """ Attr edition """
        cor = Attribute.objects.filter(name=ATTR_DEFAULT_NAME).first()
        cor.value = 'Amarelo'
        cor.save()
        self.assertEqual('Amarelo', cor.value)
    
    def test_sku_reverse_mapping(self):
        """ Associate a single SKU to a attrs (reverse natural order)"""
        cor = Attribute.objects.filter(name=ATTR_DEFAULT_NAME).last()
        sku = SKU.objects.get(name=SKU_NAME_DEFAULT)

        sku.attrs.add(cor)
        self.assertEqual( cor.sku.first().name, sku.name )

    def test_sku_category_add_attr(self):
        """ One Category for multiple attr """
        cat = Category.objects.get(name=CATEGORY_DEFAULT)
        colors = Attribute.objects.filter(name=ATTR_DEFAULT_NAME)
        cat.attrs.add(*colors)
        cat.save()
        self.assertEqual( cat.attrs.count() , COLOR_QTD )
    
    def test_sku_rm_attr(self):
        """ Removing a single attr """
        cor2 = Attribute.objects.filter(name=ATTR_DEFAULT_NAME)[randint(0,COLOR_QTD-1)]
        cor2.delete()
        self.assertEqual( Attribute.objects.filter(name=ATTR_DEFAULT_NAME).count(), COLOR_QTD-1)

    def test_sku_category_attr_rm(self):
        """ Remove a single attr from category (reversed) """
        cat = Category.objects.get(name=CATEGORY_DEFAULT)
        colors = Attribute.objects.filter(name=ATTR_DEFAULT_NAME)
        cat.attrs.add(*colors)
        cat.attrs.remove(colors[0])
        self.assertEqual( cat.count_attrs(), COLOR_QTD-1 )
    
    def test_sku(self):
        """ Associate many attrs to a single SKU """
        # 3 Categories
        cat_color = Category.objects.get(name=CATEGORY_DEFAULT)
        cat_price = Category.objects.get(name='PRICE')
        cat_price_discount = Category.objects.get(name='PRICE DISCOUNT')

        # Get attributes previously categorized
        color_attrs =  Attribute.objects.filter(name=ATTR_DEFAULT_NAME, categories__name=CATEGORY_DEFAULT)
        precos_attrs = Attribute.objects.filter(name='price', categories__name='PRICE')
        precos2_attrs = Attribute.objects.filter(name='price', categories__name='PRICE DISCOUNT')

        # Add attrs to sku
        sku = SKU.objects.get(name=SKU_NAME_DEFAULT)
        sku.attrs.add( *(list(precos_attrs) +
                         list(precos2_attrs) + 
                         list(color_attrs)))

        self.assertEqual( sku.attrs.count(), COLOR_QTD + PRICE_QTD + 1)

    def test_filtering_sku_by_price(self):
        """ Given a bunch os Attrs of category price, filter by 10 <= x <= 40 """
        sku = SKU.objects.get(name='prices')

        in_price = sku.attrs.filter( name='price', 
                                     value__number__gte=10, 
                                     value__number__lte=50)
        self.assertEqual( in_price.count(), 9 )
        self.assertEqual( float(in_price[0].value) , 10.0)