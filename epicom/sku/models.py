
from django.db import models

class Attribute(models.Model):
    """ Attributes for a product """
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True)

    def __str__(self):
        return "%s: %s" % (self.name, self.value)

    class Meta:
        """ Add a index to speed-up attributes lookup """
        indexes = [
            models.Index(fields=['name']),
        ]

class Category(models.Model):
    """ Category to organize related sku (like color, dimensions) """ 
    name  = models.CharField(unique=True, blank=True, max_length=128)
    attrs = models.ManyToManyField(Attribute,
                                related_name='categories',
                                related_query_name='categories',
                                db_table='attrs2categories' )
    
    def count_attrs(self,m_filter=models.Q()):
        return self.attrs.filter(m_filter).count()
    
    def __str__(self):
        attrs_count = self.count_attrs()
        return "%s: %d attributes" % (self.name, attrs_count)

class SKU(models.Model):
    """
        A Nested Set Modifier for a product.
    """
    # product = models.ManyToManyField('Product', 
    #                       db_name='product2sku',
    #              
    #          )
    name        = models.CharField(max_length=255, blank=True)
    created_at  = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    attrs  = models.ManyToManyField(Attribute, 
                                    related_name="sku",
                                    related_query_name='skus',
                                    db_table='attrs2skus')

    def __str__(self):
        attrs_count = self.attrs.all().count()
        return '#sku:%s: %d attributes' % (self.id, attrs_count)