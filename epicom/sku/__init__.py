from django.db.models import Lookup , DecimalField
from django.db.models.fields import Field
from django.db.models import Transform

@Field.register_lookup
class NumberValue(Transform):
    """
        Allows to cast a text to a decimal, to use database built-in query engine.
    """
    # Register this before you filter things, for example in models.py
    lookup_name = 'number'  # Used as object.filter(LeftField__number__gte, "777")
    bilateral = True        # To cast both left and right

    def as_sql(self, compiler, connection):
        sql, params = compiler.compile(self.lhs)
        sql = 'CAST(%s AS DECIMAL(10,2))' % sql
        return sql, params
    
    @property
    def output_field(self):
        return DecimalField()