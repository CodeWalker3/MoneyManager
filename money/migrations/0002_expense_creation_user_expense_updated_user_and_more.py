# Generated by Django 4.1.2 on 2022-12-04 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='creation_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='updated_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='income',
            name='creation_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='income',
            name='updated_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
    ]
