from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagePagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': int(self.page.paginator.count/self.page_size)+1,
            'results': data,
        }, status=status.HTTP_200_OK)
