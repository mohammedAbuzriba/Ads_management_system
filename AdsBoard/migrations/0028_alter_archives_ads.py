# Generated by Django 4.0.4 on 2022-05-19 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdsBoard', '0027_alter_archives_ads_alter_archives_save_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archives',
            name='ads',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archivetest', to='AdsBoard.ads'),
        ),
    ]