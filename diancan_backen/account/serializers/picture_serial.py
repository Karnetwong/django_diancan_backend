from rest_framework import serializers
from account.models import Picture

class PictureSerial(serializers.ModelSerializer):
    pic_id = serializers.CharField(max_length=10)
    pic_url = serializers.CharField(max_length=255)
    pic_message = serializers.CharField(max_length=64)
    create_time = serializers.DateTimeField()
    update_time = serializers.DateTimeField()

    class Meta:
        model = Picture
        fields =['pic_id','pic_url','pic_message','create_time','update_time']