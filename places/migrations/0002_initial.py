# Generated by Django 4.1.4 on 2023-01-08 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Accommodation', to=settings.AUTH_USER_MODEL, verbose_name='Accommodation'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='accommodation', to='places.place', verbose_name='place'),
        ),
    ]
