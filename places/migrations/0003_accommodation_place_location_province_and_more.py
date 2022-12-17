# Generated by Django 4.1.4 on 2022-12-17 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_rename_place_room_place_option_is_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='accommodation', to='places.place', verbose_name='place'),
        ),
        migrations.AddField(
            model_name='location',
            name='province',
            field=models.CharField(default='Gilan', max_length=64, verbose_name='province'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roomdateprice',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_date_price', to='places.room', verbose_name='accommodation'),
        ),
    ]