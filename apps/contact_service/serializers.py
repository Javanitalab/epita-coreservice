from apps.contact_service.models import ContactService
from rest_framework import exceptions, serializers

from apps.core.models import History


class ContactServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactService
        fields = ('__all__')
