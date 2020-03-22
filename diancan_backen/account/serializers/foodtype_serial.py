from rest_framework import serializers
from account.models import ProductCategory,ProCategory

class ProductInfoserial(serializers.ModelSerializer):
    class Meta:
        model = ProCategory
        fields = "__all__"

class Foodtypeserial(serializers.ModelSerializer):
    sub_cat = ProductInfoserial(many = True)
    class Meta:
        model = ProCategory
        fields = ['id','name','desc','category_type','create_time','update_time','sub_cat']