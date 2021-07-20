from rest_framework import serializers

from eye.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'data', 'timestamp']

    def create(self, validated_data):
        entity, is_created = Event.objects.update_or_create(**self.validated_data)
        return entity
