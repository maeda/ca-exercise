import json
from uuid import uuid4

from django.test import TransactionTestCase
from django.urls import reverse
from django.test import Client

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


PAYLOAD = {
            'session_id': 'd5c1c680-e97c-11eb-9a03-0242ac130003',
            'category': 'page interaction',
            'name': 'pageview',
            'data': {
                "host": "www.consumeraffairs.com",
                "path": "/",
            },
            'timestamp': '2021-01-01 09:15:27.243860'
        }


def event_serializer(payload=None):
    if not payload:
        payload = PAYLOAD
    serializer = EventSerializer(data=payload)
    return serializer


def save_event(payload=None):
    serializer = event_serializer(payload)
    if serializer.is_valid():
        entity = serializer.save()
        return entity


class EventSerializerTest(TransactionTestCase):
    def test_should_serialize_and_insert_data(self):
        result = save_event()
        self.assertEqual(Event.objects.get(pk=result.id), result)


class ViewsTesting(TransactionTestCase):
    def setUp(self):
        self.client = Client()

    def test_should_get_events_from_db(self):
        expected: Event = save_event()
        url = reverse('eye:event-list')
        resp = self.client.get(url)
        content = json.loads(resp.content)
        result = Event(id=expected.id, **content['results'][0])

        self.assertEqual(expected, result)

