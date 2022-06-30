from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api_product.models import Product, Category
from api_product.serializers import ProductSerializer


class LatestProductsListView(APIView):

    def get(self, request):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def search(request):
    query = request.query_params.get("query", "")
    products = {}
    if query:
        q = Q(name__icontains=query) | Q(description__icontains=query)
        products = Product.objects.filter(q)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class DetailProductView(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductByCategoryView(APIView):
    def get(self, request, category_slug):
        category = Category.objects.filter(name=category_slug)
        if category.exists():
            category = category.first()
            products = category.products.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
