# Generated by Django 4.1.4 on 2023-01-13 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flying', '0002_alter_currencyexchange_currency_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='fly_dateTime',
            new_name='fly_datetime',
        ),
        migrations.AddField(
            model_name='airline',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date join'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airline',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='is valid'),
        ),
        migrations.AddField(
            model_name='airline',
            name='last_modify',
            field=models.DateTimeField(auto_now=True, verbose_name='last modify'),
        ),
        migrations.AlterField(
            model_name='airtravel',
            name='children_price',
            field=models.FloatField(verbose_name='children_price'),
        ),
    ]
