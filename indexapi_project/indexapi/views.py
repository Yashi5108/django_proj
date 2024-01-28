# indexapi/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Min, Max
from .models import Index, DailyPrice
from .serializers import IndexSerializer, DailyPriceSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class CustomDailyPricePagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return {
            'pagination': {
                'page': self.page.number if self.page is not None else 1,
                'total_pages': self.page.paginator.num_pages if self.page is not None else 1,
                'total_rows': self.page.paginator.count if self.page is not None else len(data),
            },
            'results': data,
        }

class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer

class DailyPriceViewSet(viewsets.ModelViewSet):
    queryset = DailyPrice.objects.all()
    serializer_class = DailyPriceSerializer
    pagination_class = CustomDailyPricePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['index', 'date']
    ordering_fields = ['open_price', 'high_price', 'low_price', 'close_price', 'shares_traded', 'turnover']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Calculate data ranges
        ranges = {
            'open': {'lowest': queryset.aggregate(Min('open_price'))['open_price__min'], 'highest': queryset.aggregate(Max('open_price'))['open_price__max']},
            'high': {'lowest': queryset.aggregate(Min('high_price'))['high_price__min'], 'highest': queryset.aggregate(Max('high_price'))['high_price__max']},
            # ... Repeat for other columns
        }

        response_data = {
            'start-date': queryset.aggregate(Min('date'))['date__min'],
            'end-date': queryset.aggregate(Max('date'))['date__max'],
            'data': serializer.data,
            'pagination': self.paginator.get_paginated_response(serializer.data).data,
            'ranges': ranges
        }

        return Response(response_data)
