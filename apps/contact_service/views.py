from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from apps.contact_service.models import ContactService
from rest_framework import exceptions, serializers

from apps.contact_service.serializers import ContactServiceSerializer
from apps.core.models import History


class ContactServiceViewSet(ModelViewSet):
    queryset = ContactService.objects.all()
    serializer_class = ContactServiceSerializer


    def create(self, request, *args, **kwargs):
        endpoint = request._request.path

        current_service = ContactService.objects.filter(endpoint=endpoint)

        if not current_service:
            return Response(status=401)