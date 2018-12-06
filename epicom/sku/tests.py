from django.test import TestCase
from .models import SKUCategory, SKUAttribute, SKU

# Create your tests here.
class SkuTestCase(TestCase):
    """
        Sku CRUD Testing
    """    
    def test_instance_category(self):
        """ Creating a new sku.models.SKUCategory (in memory) """
        cat = SKUCategory(name='cor')
        self.assertEqual('cor', cat.name)

    def test_instance_attribute(self):
        """ Creating a new sku.models.SKUAttribute (in memory) """
        self.fail("SKUAttribute incomplete")

    def test_instance_sku(self):
        """ Creating a new sku.models.SKU (in memory) """
        self.fail("SKUModel incomplete")