from rest_framework import serializers
from .models import Products, Product_Materials, WareHouses, Materials


class ProductMaterialSerializer(serializers.ModelSerializer):
    material_name = serializers.CharField(source="material_id.material_name")
    warehouse_id = serializers.CharField(source="warehouse_id.id")
    price = serializers.CharField(source="warehouse_id.price")

    class Meta:
        model = Product_Materials
        fields = ("warehouse_id", "material_name", "qty", "price")


class ProductsSerializer(serializers.ModelSerializer):
    product_materials = ProductMaterialSerializer(
        source="product_materials_set", many=True
    )

    class Meta:
        model = Products
        fields = ("id", "product_name", "product_materials")
