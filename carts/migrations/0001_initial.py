# Generated by Django 4.1.4 on 2023-01-19 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlyItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
            ],
            options={
                'verbose_name': 'fly item',
                'verbose_name_plural': 'fly items',
                'db_table': 'fly_items',
            },
        ),
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
            ],
        ),
        migrations.CreateModel(
            name='PlaceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
            ],
            options={
                'verbose_name': 'place item',
                'verbose_name_plural': 'place items',
                'db_table': 'place_items',
            },
        ),
        migrations.CreateModel(
            name='PlaceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'cancel'), (1, 'unpaid'), (2, 'paid'), (3, 'payment failed')], default=0, verbose_name='status')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='create_date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='update date')),
            ],
            options={
                'verbose_name': 'place order',
                'verbose_name_plural': 'place orders',
                'db_table': 'place_orders',
            },
        ),
    ]
