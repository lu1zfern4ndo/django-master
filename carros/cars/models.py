from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField()

    def __str__(self) -> str:
        return f'{self.model} = {self.brand}'
