from django.contrib.auth.models import User
from rest_framework import serializers
from news.models import News

# class SerializerNews(serializers.Serializer):

class SerializerNews(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


    def validate(self, data):
        if not User.objects.filter(username=data['author']):
            raise serializers.ValidationError("Maaf Author id salah")

        return data

