# Generated by Django 3.2.6 on 2021-08-16 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='art',
            old_name='year',
            new_name='date',
        ),
    ]
