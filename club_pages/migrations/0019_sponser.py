# Generated by Django 2.0 on 2018-04-24 10:45

import club_pages.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_pages', '0018_auto_20180419_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=club_pages.models.upload_player_image)),
            ],
        ),
    ]
