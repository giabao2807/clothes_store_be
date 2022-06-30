from rest_framework.serializers import ModelSerializer

from api_product.models import Category
from api_product.serializers import ProductSerializer


class CategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "get_absolute_url",
            "products",
        ]