from django.contrib import admin
from .models import Products, Product_Materials, WareHouses, Materials


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "product_code",
    )
    search_fields = ("product_name",)


@admin.register(Product_Materials)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_id",
        "material_id",
        "warehouse_id",
        "qty",
    )
    search_fields = ("product_id",)


@admin.register(WareHouses)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "material_id",
        "remainder",
        "price",
    )
    search_fields = ("material_id",)


@admin.register(Materials)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "material_name",
    )
    search_fields = ("material_name",)
