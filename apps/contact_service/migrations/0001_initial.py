# Generated by Django 4.2.11 on 2024-05-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.CharField(default=None, max_length=256, null=True)),
                ('last_communication', models.DateTimeField(default=None, null=True)),
            ],
        ),
    ]
