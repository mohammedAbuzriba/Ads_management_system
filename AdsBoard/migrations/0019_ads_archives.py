# Generated by Django 4.0.4 on 2022-05-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdsBoard', '0018_archives'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='Archives',
            field=models.BooleanField(default=False),
        ),
    ]
