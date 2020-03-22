from rest_framework import serializers
from account.models import OrderMaster,OrderDetail

class OderDetailSerial(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['order_id','product_name','product_price','product_icon','product_quantity']

class OrderlistSerial(serializers.ModelSerializer):
    master_detail = OderDetailSerial(many=True,read_only=True)
    class Meta:
        model = OrderMaster
        fields = ['order_id','buyer_name','buyer_phone',
                  'buyer_address','buyer_openid',
                  'order_amount','order_status','buyer_name','create_time','master_detail','orderStatusStr']

