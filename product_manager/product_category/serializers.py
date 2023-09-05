from product_category.models import ProductCategoryModel
from rest_framework import serializers


class ProductCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = "__all__"
