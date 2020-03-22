from rest_framework import serializers
from account.models import Comment


class CommentSerial(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
