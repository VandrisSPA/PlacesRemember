# Generated by Django 3.1.4 on 2020-12-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0009_auto_20201221_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='feelings',
            field=models.CharField(default='', max_length=100),
        ),
    ]
