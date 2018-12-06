from django.test import TestCase
from .models import Category, Attribute, SKU

# Create your tests here.
class SkuTestCase(TestCase):
    """
        Sku CRUD Testing
    """
    def setUp(self):
        cor = Attribute.objects.create(name='cor',value='Azul')
        cat = Category.objects.create(name='cores')
    
    def test_sku_attribute_change(self):
        """ SKUAttr edit """
        cor = Attribute.objects.get(name='cor')
        self.assertEqual('cor', cor.name)
        self.assertEqual('Azul',cor.value)
        cor.value = 'Amarelo'
        cor.save()
        self.assertEqual('Amarelo', cor.value)

    def test_sku_category_add_attr(self):
        """ Category for attributes """
        cat = Category.objects.get(name='cores')
        cor = Attribute.objects.get(name='cor')
        cat.attrs.add(cor)
        cat.save()
        self.assertEqual( cor.categories.first().name , cat.name )

    def test_sku_attribute_search(self):
        pass

    def test_instance_sku(self):
        """ Creating a new sku.models.SKU (in memory) """
        self.fail("SKUModel TODO")