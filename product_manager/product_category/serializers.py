from product_category.models import ProductCategoryModel
from rest_framework import serializers


class ContactModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = "__all__"
