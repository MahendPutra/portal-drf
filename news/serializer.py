from django.utils.timesince import timesince
from django.contrib.auth.models import User
from rest_framework import serializers
from news import models

# serializers.ModelSerializer
# serializers.Serializer

class NewsSerializer(serializers.ModelSerializer):
    
    # author = serializers.SerializerMethodField('get_author', write_only=False)
    created_at = serializers.SerializerMethodField('get_created', read_only=True, write_only=False)

    class Meta:
        model = models.News
        fields = ('author', 'title', 'content', 'category', 'cover', 'created_at')
        # exclude = ('cover',)

    def get_created(self, obj):
        return timesince(obj.created_at)

    # def get_author(self, obj):
    #     return {
    #         "id": obj.author.id,
    #         "first_name": obj.author.first_name,
    #         "last_name": obj.author.last_name,
    #         "email": obj.author.email,
    #         "date_joined": obj.author.date_joined,
    #     }