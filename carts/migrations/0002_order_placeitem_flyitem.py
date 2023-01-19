# Generated by Django 4.1.4 on 2023-01-19 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flying', '0007_flyticket'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0005_alter_placedateprice_extra_price'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'cancel'), (1, 'unpaid'), (2, 'paid'), (3, 'payment failed')], default=0, verbose_name='status')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('total_price', models.FloatField(blank=True, null=True, verbose_name='total price')),
                ('currency', models.PositiveSmallIntegerField(choices=[(1, 'IRR'), (2, 'USD'), (3, 'EUR'), (4, 'CAD')], default=1, verbose_name='currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('items', models.ManyToManyField(blank=True, null=True, related_name='place_items', to='flying.flyticket')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='place_item', to='carts.order')),
            ],
            options={
                'verbose_name': 'place item',
                'verbose_name_plural': 'place items',
                'db_table': 'place_items',
            },
        ),
        migrations.CreateModel(
            name='FlyItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('items', models.ManyToManyField(blank=True, null=True, related_name='fly_items', to='places.placedateprice')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fly_item', to='carts.order')),
            ],
            options={
                'verbose_name': 'fly item',
                'verbose_name_plural': 'fly items',
                'db_table': 'fly_items',
            },
        ),
    ]
