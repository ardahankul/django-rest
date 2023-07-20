from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from post.models import Post
from .serializers import PostSerializer,PostCreateUpdateSerializer
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from .permissions import IsOwner
#from rest_framework.filters import SearchFilter,OrderingFilter


"""
class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer

    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title'] http://example.com/api/users?search=russell&ordering=title  --> returns objects that title includes russel, order by title


    def get_queryset(self):
        queryset = Post.objects.filter(draft=False)  --> query filter 

    
"""

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'  #this field sets url with slug (default  is pk)

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug' 
    permission_classes = [IsOwner]


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug' 
    permission_classes = [IsOwner]
 
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)