from rest_framework import serializers
from post.models import Post
from comment.api.serializers import CommentPostListSerializer

class PostSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug' 
    )

    username = serializers.SerializerMethodField(method_name='username_new')
    post_comment = CommentPostListSerializer(many=True,read_only=True)

    class Meta: 
        model = Post
        fields = [ 
            'id',
            'username',
            'title',
            'content',
            'url',
            'created',
            'image',
            'modified_by',
            'post_comment',
        ]
    
    def username_new(self, obj):
        return str(obj.user.username)


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]        