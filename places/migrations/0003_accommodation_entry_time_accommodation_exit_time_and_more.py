# Generated by Django 4.1.4 on 2022-12-14 13:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='entry_time',
            field=models.TimeField(default=datetime.time(12, 0), verbose_name='entry time'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='exit_time',
            field=models.TimeField(default=datetime.time(14, 0), verbose_name='exit time'),
        ),
        migrations.CreateModel(
            name='DatePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reserve', models.BooleanField(default=False, verbose_name='is reserve')),
                ('date', models.DateField(verbose_name='date')),
                ('price', models.FloatField(verbose_name='price')),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='date_price', to='places.accommodation', verbose_name='accommodation')),
            ],
        ),
    ]
