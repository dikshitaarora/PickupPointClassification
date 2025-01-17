# Generated by Django 3.0.3 on 2020-06-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='no_of_cctv',
            new_name='google_rating',
        ),
        migrations.AddField(
            model_name='address',
            name='country_code',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='time_zone',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
