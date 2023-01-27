import django_filters

from reviews.models import Title


class TitlesFilter(django_filters.FilterSet):
    """
    Фильтрация произведений по имени, категории, жанру, году.
    """
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='contains'
    )
    category = django_filters.CharFilter(
        field_name='category__slug',
        lookup_expr='contains'

    )
    genre = django_filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='contains'
    )

    class Meta:
        model = Title
        fields = ('name', 'genre', 'category', 'year')
