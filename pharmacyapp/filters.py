import django_filters
from .models import Category, Product

class Product_filter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = ['medicineName']


class Category_filter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name']       