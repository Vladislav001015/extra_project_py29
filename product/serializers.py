from rest_framework import serializers
from product.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)


