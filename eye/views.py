from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from eye.models import Event
from eye.serializers import EventSerializer


class ListEvents(ModelViewSet):

    queryset = Event.objects.select_for_update().all().order_by('-timestamp')
    serializer_class = EventSerializer

    @transaction.atomic
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
