from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Products(models.Model):
    product_name = models.CharField(max_length=10_000)
    product_code = models.TextField(null=True)

    def __str__(self):
        return self.product_code

    class Meta:
        verbose_name = "product"


class Materials(models.Model):
    material_name = models.CharField(max_length=10_000)

    def __str__(self):
        return self.material_name

    class Meta:
        verbose_name = "material"


class WareHouses(models.Model):
    material_id = models.ForeignKey(Materials, on_delete=models.CASCADE)
    remainder = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return str(self.remainder)

    class Meta:
        verbose_name = "ware_house"


class Product_Materials(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Materials, on_delete=models.CASCADE)
    warehouse_id = models.ForeignKey(WareHouses, on_delete=models.CASCADE)
    qty = models.FloatField()

    def __str__(self):
        return str(self.qty)

    class Meta:
        verbose_name = "product_material"


@receiver(post_save, sender=Product_Materials)
def update_warehouse(sender, instance, created, **kwargs):
    if created:
        warehouse = instance.warehouse_id
        warehouse.remainder -= instance.qty
        warehouse.save()
