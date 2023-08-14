from rest_framework import serializers
from post.models import Post
from comment.api.serializers import CommentPostListSerializer

class PostSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug' 
    )

    #username = serializers.SerializerMethodField(method_name='username_new')
    post_comment = CommentPostListSerializer(many=True,read_only=True)
    # if u need user as objects try this =>  user = UserCommentSerializer()  #import from comment.api.serializer
    # note : post_comment returns user objects already! 

    favorite_count = serializers.SerializerMethodField()

    class Meta: 
        model = Post
        fields = [ 
            'id',
            'user',     
            'title',
            'content',
            'url',
            'created',
            'image',
            'modified_by',
            'post_comment',
            'favorite_count'
        ]
    
    def username_new(self, obj):
        return str(obj.user.username)
    
    def get_favorite_count(self, obj):
        # Get the count of favorites for the current post using the RelatedManager
        return obj.favorites.count()


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]        