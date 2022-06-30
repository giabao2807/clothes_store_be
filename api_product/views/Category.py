from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_product.models import Category
from api_product.serializers import CategorySerializer


class CategoryProductView(APIView):
    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)