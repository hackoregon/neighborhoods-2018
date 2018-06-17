from rest_framework.pagination import LimitOffsetPagination

class LargeResultSetPagination(LimitOffsetPagination):
    max_limit = 5000