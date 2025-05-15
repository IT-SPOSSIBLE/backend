from drf_api.base import BaseListCreateAPIView, BaseRetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializer

class ProductCreateListAPIView(BaseListCreateAPIView):
    model = Product
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = Product
    serializer_class = ProductSerializer