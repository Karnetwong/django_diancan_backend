from rest_framework import serializers
from account.models import ProductInfo,ProCategory

class Productlistserial(serializers.ModelSerializer):
    class Meta:
        model = ProCategory
        fields = "__all__"
