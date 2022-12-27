# Generated by Django 4.1.4 on 2022-12-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flying', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='is valid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
                ('last_modify', models.DateTimeField(auto_now=True, verbose_name='last modify')),
                ('national_symbol', models.CharField(max_length=8, unique=True, verbose_name='national symbol')),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
                'db_table': 'currency',
            },
        ),
    ]