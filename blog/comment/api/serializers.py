from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from django.contrib.auth.models import User
from post.models import Post
from comment.models import Comment

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created',]      #instead of define fields, accept all fields except created!

    def validate(self, attrs):
        if(attrs["parent"]):
            if(attrs["parent"].post != attrs["post"]):
                raise serializers.ValidationError("Something went wrong")
        return attrs
    
    def perform_create(self,serializer):
        serializer.save(user = self.request.user)

class UserCommentSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email',]

class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','slug',]

class CommentPostListSerializer(ModelSerializer):   #this is the serializer to get comments while getting posts
    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self,obj):
        if obj.any_children:
            return CommentPostListSerializer(obj.children(), many=True).data

class CommentListSerializer(ModelSerializer):

    replies = SerializerMethodField()
    user = UserCommentSerializer()
    post = PostCommentSerializer()
    

    class Meta:
        model = Comment
        fields = '__all__'      #to get all fileds 

    def get_replies(self,obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data
        
class CommentDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]
        


