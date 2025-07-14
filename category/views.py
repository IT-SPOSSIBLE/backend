from drf_api.base import BaseListCreateAPIView, BaseRetrieveUpdateDestroyAPIView
from .serializers import CategorySerializer
from .models import Category
from rest_framework.permissions import IsAuthenticated

class CategoryListCreateAPIView(BaseListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryRetrieveUpdateDestroyAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerializer