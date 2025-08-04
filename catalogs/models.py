from django.db import models


class Item(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=4000)
    unit = models.CharField(max_length=10)
    source = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=18, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sinapi_item'

    def __str__(self):
        return self.code
