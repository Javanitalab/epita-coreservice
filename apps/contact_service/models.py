from django.db import models


class ContactService(models.Model):
    endpoint = models.CharField(max_length=256, null=True, default=None)
    last_communication = models.DateTimeField(null=True, default=None)
