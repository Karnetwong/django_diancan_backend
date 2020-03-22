from rest_framework import serializers
from account.models import OrderDetail

class OderDetailSerial(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['order_id','product_name','product_price','product_icon','product_quantity']