from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.


class User(AbstractUser):
    age = models.IntegerField(null=True)
    street = models.CharField(max_length=255, null=True)

    # Specify related_name to avoid clashes with auth.User
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='api_user_permissions',
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='api_user_groups',
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    trigger_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
