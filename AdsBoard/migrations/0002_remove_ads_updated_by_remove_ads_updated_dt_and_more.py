# Generated by Django 4.0.4 on 2022-04-27 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdsBoard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='updated_dt',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='views',
        ),
    ]
