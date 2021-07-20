import json
from uuid import uuid4

from django.test import TransactionTestCase

from eye.models import Event
from eye.serializers import EventSerializer


class EventModelTest(TransactionTestCase):
    def test_should_save_an_event(self):
        event = Event(
            session_id=uuid4(),
            category='page interaction',
            name='pageview',
            data={
                "host": "www.consumeraffairs.com",
                "path": "/",
            },
            timestamp="2021-01-01 09:15:27.243860"
        )
        self.assertCountEqual(Event.objects.all(), [])
        event.save()
        self.assertCountEqual(Event.objects.all(), [event])


class EventSerializerTest(TransactionTestCase):
    def test_should_serialize_and_insert_data(self):
        payload = {
            'session_id': 'd5c1c680-e97c-11eb-9a03-0242ac130003',
            'category': 'page interaction',
            'name': 'pageview',
            'data': {
                "host": "www.consumeraffairs.com",
                "path": "/",
            },
            'timestamp': '2021-01-01 09:15:27.243860'
        }

        serializer = EventSerializer(data=payload)
        if serializer.is_valid():
            result = serializer.save()
            self.assertEqual(Event.objects.get(pk=result.id), result)
