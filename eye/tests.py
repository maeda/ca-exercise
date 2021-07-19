from uuid import uuid4

from django.test import TransactionTestCase

from eye.models import Event


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
