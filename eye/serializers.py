import datetime
import logging as logger
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from eye.models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'data', 'timestamp']

    def create(self, validated_data):
        entity, is_created = Event.objects.update_or_create(**self.validated_data)
        return entity

    def validate(self, attrs):
        if 'timestamp' in attrs:
            timestamp = attrs['timestamp']
            now = datetime.datetime.now(tz=timestamp.tzinfo)
            if attrs['timestamp'] > now:
                raise serializers.ValidationError({
                    'timestamp': 'timestamp date cannot be greater and current datetime.'
                })
        return super(EventSerializer, self).validate(attrs)

    def is_valid(self, raise_exception=False):
        ret = super(EventSerializer, self).is_valid(False)
        if self._errors:
            logger.warning("Serialization failed due to {}".format(self.errors))
            if raise_exception:
                raise ValidationError(self.errors)
        return ret
