# Generated by Django 2.0 on 2018-04-19 14:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_pages', '0011_auto_20180419_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicdata',
            name='footer_col_1',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dynamicdata',
            name='footer_col_2',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dynamicdata',
            name='footer_col_3',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
