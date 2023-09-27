from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    # TODO: видеть только свои продукты
