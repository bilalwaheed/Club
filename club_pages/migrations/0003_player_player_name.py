# Generated by Django 2.0.2 on 2018-03-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_pages', '0002_auto_20180306_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_name',
            field=models.CharField(default='SOME STRING', max_length=250),
        ),
    ]
