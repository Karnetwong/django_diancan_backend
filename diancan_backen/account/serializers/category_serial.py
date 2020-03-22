from rest_framework import serializers
from account.models import ProductInfo,ProductCategory


class ProductCategorySerial(serializers.ModelSerializer):
    class Meta:
        model =ProductInfo
        fields = "__all__"


class ProductCategorySerial(serializers.ModelSerializer):
    sub_cat = ProductCategorySerial(many=True,read_only=True)
    class Meta:
        model =ProductCategory
        fields = ['category_id','category_name','category_type','create_time','update_time','sub_cat']