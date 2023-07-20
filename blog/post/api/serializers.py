from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = [
            'user',
            'title',
            'content',
            'slug',
            'created',
            'image',
            'modified_by',
        ]

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]        