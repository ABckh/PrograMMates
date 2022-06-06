from .models import *
from django import forms
import django_filters


class AdvertFilter(django_filters.FilterSet):
    title = django_filters.ChoiceFilter(field_name='title', label='Programming language', empty_label='Not selected',
                                        choices=PROGRAMMING_LANGUAGES,
                                        widget=forms.Select(attrs={'class': 'form-input'}))
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains',
                                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    language = django_filters.ChoiceFilter(field_name='username__language', label='Language',
                                           empty_label='Not selected', lookup_expr='icontains', choices=LANGUAGES,
                                           widget=forms.Select(attrs={'class': 'form-input'}))

    class Meta:
        model = Advert
        fields = ['title', 'description', 'language']
