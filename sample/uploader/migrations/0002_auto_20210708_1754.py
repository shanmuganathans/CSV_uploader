# Generated by Django 3.2.5 on 2021-07-08 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='last_name',
            new_name='lastname',
        ),
    ]