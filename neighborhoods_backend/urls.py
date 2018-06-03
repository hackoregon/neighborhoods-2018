from rest_framework_swagger.views import get_swagger_view

"""neighborhoods_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

schema_view = get_swagger_view(title='Hack Oregon 2018 Neighborhood Development APIs')

urlpatterns = [
    path('neighborhood-development/', schema_view),
    path('neighborhood-development/api/', include('api.urls')),
    path('neighborhood-development/census/', include('census.urls')),
]
