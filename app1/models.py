from django.db import models
from django.utils import timezone


class Deal(models.Model):
    customer = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    total = models.IntegerField()

    class Meta:
        ordering = ['customer']

    def __str__(self):
        return self.customer