# Generated by Django 4.0.4 on 2022-04-30 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdsBoard', '0007_section_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
