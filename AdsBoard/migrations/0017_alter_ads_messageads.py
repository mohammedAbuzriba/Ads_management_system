# Generated by Django 4.0.4 on 2022-05-07 09:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdsBoard', '0016_alter_ads_messageads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='messageAds',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
