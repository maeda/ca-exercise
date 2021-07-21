import logging as logger

from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from eye.filters import EventFilter
from eye.models import Event
from eye.serializers import EventSerializer


class ListEvents(ModelViewSet):

    queryset = Event.objects.select_for_update().all().order_by('-timestamp')
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['session_id', 'category']
    filter_class = EventFilter

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        logger.info(request.data)
        return super(ModelViewSet, self).create(request, *args, **kwargs)

