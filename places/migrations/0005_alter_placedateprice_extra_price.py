# Generated by Django 4.1.4 on 2023-01-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_placedateprice_person_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedateprice',
            name='extra_price',
            field=models.FloatField(default=0, verbose_name='extra price'),
        ),
    ]
