# Generated by Django 3.0.3 on 2021-04-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20210423_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cost',
            field=models.CharField(default='', max_length=255),
        ),
    ]
