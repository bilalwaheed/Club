# Generated by Django 2.0 on 2018-05-03 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club_pages', '0021_auto_20180503_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixtureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='fixture',
            name='fixture_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='club_pages.FixtureType'),
        ),
    ]