from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField()
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self) -> str:
        return self.model
