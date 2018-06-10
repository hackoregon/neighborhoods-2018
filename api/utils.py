"""
General utility functions used elsewhere.
"""


def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    See: https://docs.djangoproject.com/en/2.0/topics/db/sql/#executing-custom-sql-directly
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]