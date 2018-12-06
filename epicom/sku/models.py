from django.db import models

class SKUCategory(models.Model):
    """ Category to organize related sku (like color, dimensions) """ 
    name = models.CharField(unique=True, blank=True, max_length=128)

class SKUAttribute(models.Model):
    """ Attributes for a product """
    name = models.CharField(unique=True, max_length=255)
    valor = models.TextField(blank=True)
    category = models.ForeignKey(SKUCategory,
                                on_delete=models.SET_NULL,
                                null=True )

class SKU(models.Model):
    """
        A Nested Set Modifier for a product.
    """
    # product = models.ManyToManyField('Product', 
    #                       db_name='product2sku',
    #                       )
    created_at  = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    parameters  = models.ManyToManyField(SKUAttribute, 
                                    related_name="attribute",
                                    related_query_name="attributes",
                                    db_table='sku2attributes')

    def __str__(self):
        return '#sku:{self.id}'