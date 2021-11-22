# Generated by Django 3.2.8 on 2021-11-17 12:48

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '0002_event_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Event Start Time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='staff',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Staff Attending Event'),
        ),
    ]