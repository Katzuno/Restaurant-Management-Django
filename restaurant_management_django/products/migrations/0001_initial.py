# Generated by Django 3.0.7 on 2020-07-04 14:14

import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of the product')),
                ('description', models.CharField(blank=True, max_length=1024, verbose_name='Description of the product')),
                ('nutritional_values', django.contrib.postgres.fields.hstore.HStoreField(blank=True, verbose_name='Nutritional values of the product')),
                ('status', models.CharField(choices=[('INACTIVE', 'Inactive'), ('ACTIVE', 'Active')], default='ACTIVE', max_length=8)),
            ],
        ),
    ]
