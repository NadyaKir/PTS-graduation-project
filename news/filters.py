import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from django import forms
from news.models import GVS


class FindGVSItem(django_filters.FilterSet):
    street = CharFilter(field_name="street", lookup_expr='icontains', label='Улица',
                        widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    build = CharFilter(field_name="build", lookup_expr='icontains', label='Дом',
                       widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))

    class Meta:
        model = GVS
        fields = ['street', 'build']
