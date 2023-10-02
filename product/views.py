from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer
from django.views.generic import ListView


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    # def get_queryset(self):
    #     queryset = super().get_queryset()
        
    #     # print(self.request.user)
    #     queryset = queryset.filter(owner=self.request.user)  # Вытащили только свои продукты
    #     return queryset


class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
