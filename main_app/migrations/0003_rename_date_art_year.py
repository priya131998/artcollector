# Generated by Django 3.2.6 on 2021-08-16 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_year_art_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='art',
            old_name='date',
            new_name='year',
        ),
    ]
