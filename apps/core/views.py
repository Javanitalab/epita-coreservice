import datetime

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from apps.contact_service.connector import ContactServiceConnector
from apps.contact_service.models import ContactService
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


class ContactServiceViewSet(ViewSet):

    @action(detail=False, methods=['get'])
    def create_contact(self, request, *args, **kwargs):
        endpoint = self.request.query_params.get('endpoint', None)

        contact_service = ContactService.objects.last()
        contact_service_connector = ContactServiceConnector(endpoint='http://localhost:8001')
        if contact_service.endpoint:
            success = contact_service_connector.send_ping(contact_service.endpoint)
            if success:
                ContactService.objects.create(last_communication=datetime.datetime.now(), endpoint=endpoint)
            else:
                ContactService.objects.create(last_communication=datetime.datetime.now(), endpoint=None)
                return Response(status=503, data={'service not found'})

            response = contact_service_connector.create_contact(contact_service.endpoint, self.request.data)

            return response
        return Response(status=201)
