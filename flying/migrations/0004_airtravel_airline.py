# Generated by Django 4.1.4 on 2023-01-13 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flying', '0003_rename_fly_datetime_flight_fly_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='airtravel',
            name='airline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airline_airline', to='flying.airline', verbose_name='airline'),
        ),
    ]