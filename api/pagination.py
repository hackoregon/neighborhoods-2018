from rest_framework.pagination import LimitOffsetPagination

class LargeResultSetPagination(LimitOffsetPagination):
    max_limit = 5000


class VeryLargeResultSetPagination(LimitOffsetPagination):
    max_limit = 50000