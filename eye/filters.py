import django_filters

from eye.models import Event


class EventFilter(django_filters.FilterSet):

    class Meta:
        model = Event
        fields = {
            'timestamp': ['gte', 'lt']
        }
