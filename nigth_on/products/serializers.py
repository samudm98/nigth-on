from rest_framework.serializers import ModelSerializer
from nigth_on.products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'image', 'is_service')


