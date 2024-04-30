import datetime

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from apps.core.models import History
from apps.core.serializers import HistorySerializer


# Create your views here.


class HistoryViewSet(ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer



class HistoryTwoViewSet(ViewSet):

    @action(detail=False, methods=['post'])
    def create_history(self, request, *args, **kwargs):
        user_id = self.request.data.get('user', None)
        description = self.request.data.get('description', None)
        history = History.objects.create(user_id, description=description)

        return Response(
            status=201,
            data={
                'id': history.id,
                'description': history.description,
                'trigger_date': history.trigger_date.strftime('y%-m%-d-%'),
            })
