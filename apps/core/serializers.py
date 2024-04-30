from rest_framework import exceptions, serializers

from apps.core.models import History


class HistorySerializer(serializers.Serializer):
    class Meta:
        model = History
        fields = ('__all__')
        # fields = ['user,description']
        # exclude = ['trigger_date']


class UserHistorySerializer(serializers.Serializer):
    class Meta:
        model = History
        # fields = ('__all__')
        fields = ['user']
        # exclude = ['trigger_date']
