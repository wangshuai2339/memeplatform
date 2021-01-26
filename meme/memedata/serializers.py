from rest_framework import serializers
from memedata.models import TestUser,TestStar

# class TestUserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()


class TestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestUser
        # fields = ("username", "password")
        fields = "__all__"

class TestStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestStar
        # fields = ("username", "password")
        fields = "__all__"