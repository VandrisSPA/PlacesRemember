# Generated by Django 3.1.4 on 2020-12-19 15:20

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testapp', 'enable_postgis'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.CharField(max_length=100)),
                ('field3', models.IntegerField(default=-1)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, default=django.contrib.gis.geos.point.Point(0.0, 0.0), srid=4326)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
