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
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = serializer.save()
        return Response(response, status=status.HTTP_201_CREATED)

