from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView
from favorite.models import Favorite 
from .serializers import FavoriteCreateSerializer
from .permissons import IsOwner
from rest_framework.permissions import IsAuthenticated


class FavoriteCreateAPIView(CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class FavoriteListAPIView(ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateSerializer
    permission_classes = [IsAuthenticated]

class FavoriteDeleteAPIView(DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]