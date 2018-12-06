
from django.db import models

class Attribute(models.Model):
    """ Attributes for a product """
    name = models.CharField(unique=True, max_length=255)
    value = models.TextField(blank=True)

    def __str__(self):
        return '{self.name}: {self.value}'

class Category(models.Model):
    """ Category to organize related sku (like color, dimensions) """ 
    name  = models.CharField(unique=True, blank=True, max_length=128)
    attrs = models.ManyToManyField(Attribute,
                                related_name='categories',
                                db_table='attrs2categories' )
    
    def __str__(self):
        attrs_count = self.attrs.all().count()
        return '{self.name}: {attrs_count} attributes'

class SKU(models.Model):
    """
        A Nested Set Modifier for a product.
    """
    # product = models.ManyToManyField('Product', 
    #                       db_name='product2sku',
    #                       )
    created_at  = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    attributes  = models.ManyToManyField(Attribute, 
                                    related_name="attrs",
                                    related_query_name='skus',
                                    db_table='attrs2skus')

    def __str__(self):
        attrs_count = self.attrs.all().count()
        return '#sku:{self.id}: {attrs_count} attributes'