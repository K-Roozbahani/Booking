# Generated by Django 4.1.4 on 2023-01-05 06:41

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
                ('base_price', models.FloatField(verbose_name='base price')),
                ('currency', models.PositiveIntegerField(choices=[(1, 'IRR'), (2, 'USD'), (3, 'EUR'), (4, 'CAD')], verbose_name='currency')),
                ('extra_person_price', models.FloatField(verbose_name='extra person price')),
                ('standard_capacity', models.IntegerField(verbose_name='standard capacity')),
                ('maximum_capacity', models.IntegerField(verbose_name='maximum capacity')),
                ('entry_time', models.TimeField(default=datetime.time(12, 0), verbose_name='entry time')),
                ('exit_time', models.TimeField(default=datetime.time(14, 0), verbose_name='exit time')),
                ('area_size', models.IntegerField(verbose_name='area size')),
                ('build_size', models.IntegerField(verbose_name='build size')),
                ('is_charter', models.BooleanField(default=True, verbose_name='is charter')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'accommodation',
                'verbose_name_plural': 'accommodations',
                'db_table': 'accommodation',
            },
        ),
        migrations.CreateModel(
            name='AccommodationAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
                ('description', models.CharField(blank=True, max_length=64, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'accommodation attribute',
                'verbose_name_plural': 'accommodations attribute',
                'db_table': 'accommodation_attributes',
            },
        ),
        migrations.CreateModel(
            name='AccommodationRoomAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
                ('description', models.CharField(blank=True, max_length=64, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'accommodation room attribute',
                'verbose_name_plural': 'accommodations rooms attribute',
                'db_table': 'room_attributes',
            },
        ),
        migrations.CreateModel(
            name='AccommodationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
            ],
            options={
                'verbose_name': 'accommodation type',
                'verbose_name_plural': 'accommodations type',
                'db_table': 'accommodation_type',
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('description', models.CharField(default='end weak', max_length=64, verbose_name='description')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last_update')),
            ],
            options={
                'verbose_name': 'holiday',
                'verbose_name_plural': 'holidays',
                'db_table': 'holidays',
            },
        ),
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
                ('room_number', models.PositiveIntegerField(verbose_name='room number')),
                ('size', models.IntegerField(verbose_name='size')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('base_price', models.FloatField(blank=True, null=True, verbose_name='bace price')),
                ('currency', models.PositiveIntegerField(choices=[(1, 'IRR'), (2, 'USD'), (3, 'EUR'), (4, 'CAD')], verbose_name='currency')),
                ('room_star', models.PositiveIntegerField(default=2, validators=[django.core.validators.MaxValueValidator(5)], verbose_name='room star')),
                ('capacity', models.PositiveSmallIntegerField(default=2, verbose_name='capacity')),
            ],
            options={
                'verbose_name': 'hotel_room',
                'verbose_name_plural': 'hotels_rooms',
                'db_table': 'hotel_room',
            },
        ),
        migrations.CreateModel(
            name='HotelRoomAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
                ('description', models.CharField(blank=True, max_length=64, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'hotel room attribute',
                'verbose_name_plural': 'hotels room attribute',
                'db_table': 'hotel_room_attributes',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=64, verbose_name='country')),
                ('province', models.CharField(max_length=64, verbose_name='province')),
                ('city', models.CharField(max_length=64, verbose_name='city')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
            ],
            options={
                'verbose_name': 'location type',
                'verbose_name_plural': 'locations type',
                'db_table': 'location_type',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
            ],
            options={
                'verbose_name': 'room type',
                'verbose_name_plural': 'rooms type',
                'db_table': 'room_type',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
                ('address', models.TextField(verbose_name='address')),
                ('place_type', models.PositiveSmallIntegerField(choices=[(3, 'hotel'), (2, 'motel'), (3, 'hostel'), (4, 'vila'), (5, 'holiday camp'), (6, 'room')], verbose_name='place_type')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='place_location', to='places.location', verbose_name='location')),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
                'db_table': 'Place',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
                ('is_free', models.BooleanField(default=True, verbose_name='is free')),
                ('price', models.FloatField(default=0, verbose_name='price')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='places.place', verbose_name='place')),
            ],
            options={
                'verbose_name': 'option',
                'verbose_name_plural': 'options',
                'db_table': 'option',
            },
        ),
        migrations.CreateModel(
            name='HotelRoomDatePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.PositiveIntegerField(choices=[(1, 'IRR'), (2, 'USD'), (3, 'EUR'), (4, 'CAD')], verbose_name='currency')),
                ('is_reserve', models.BooleanField(default=False, verbose_name='is reserve')),
                ('date', models.DateField(verbose_name='date')),
                ('price', models.FloatField(verbose_name='price')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='date_price', to='places.hotelroom', verbose_name='accommodation')),
            ],
            options={
                'verbose_name': 'hotel room date price',
                'verbose_name_plural': 'hotel rooms dates price',
                'db_table': 'hotel_room_date_price',
            },
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='attribute',
            field=models.ManyToManyField(related_name='hotel_room', to='places.hotelroomattribute', verbose_name='attribute'),
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_room', to='places.place', verbose_name='place'),
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_room', to='places.roomtype', verbose_name='room_type'),
        ),
        migrations.CreateModel(
            name='AccommodationRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
                ('size', models.IntegerField(blank=True, null=True, verbose_name='size')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('accommodation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room', to='places.accommodation', verbose_name='accommodation')),
                ('attribute', models.ManyToManyField(related_name='accommodation_room', to='places.accommodationroomattribute', verbose_name='attribute')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accommodation_room', to='places.roomtype', verbose_name='room_type')),
            ],
            options={
                'verbose_name': 'accommodation room',
                'verbose_name_plural': 'accommodations room',
                'db_table': 'accommodation_room',
            },
        ),
        migrations.CreateModel(
            name='AccommodationDatePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.PositiveIntegerField(choices=[(1, 'IRR'), (2, 'USD'), (3, 'EUR'), (4, 'CAD')], verbose_name='currency')),
                ('is_reserve', models.BooleanField(default=False, verbose_name='is reserve')),
                ('date', models.DateField(verbose_name='date')),
                ('price', models.FloatField(verbose_name='price')),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='date_price', to='places.accommodation', verbose_name='accommodation')),
            ],
            options={
                'verbose_name': 'accommodation date price',
                'verbose_name_plural': 'accommodation dates price',
                'db_table': 'accommodation_date_price',
            },
        ),
        migrations.AddField(
            model_name='accommodation',
            name='accommodation_type',
            field=models.ManyToManyField(related_name='accommodation', to='places.accommodationtype', verbose_name='accommodation type'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='attribute',
            field=models.ManyToManyField(related_name='accommodation', to='places.accommodationattribute', verbose_name='attribute'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='location_type',
            field=models.ManyToManyField(related_name='accommodation', to='places.locationtype', verbose_name='location type'),
        ),
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
