# Generated by Django 4.1.4 on 2023-01-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flying', '0005_airtravel_fly_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airtravel',
            name='currency',
            field=models.PositiveSmallIntegerField(choices=[(1, 'IRR'), (2, 'USD'), (3, 'EUR'), (4, 'CAD')], default=1, verbose_name='currency'),
        ),
    ]