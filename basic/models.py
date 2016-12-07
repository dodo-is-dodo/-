from django.db import models, migrations
from django.contrib.postgres import fields

class Store(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    lat = models.DecimalField(max_digits=20, decimal_places=10)
    lon = models.DecimalField(max_digits=20, decimal_places=10)
    inventory = fields.JSONField()

    class Meta:
        ordering = ('sid',)


