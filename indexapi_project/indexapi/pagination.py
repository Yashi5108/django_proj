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
